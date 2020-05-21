from django.shortcuts import render
from django.http import JsonResponse
from .utils import db_entry as db
from .utils import auth
from .social_media import validators, twitter
from flask import jsonify
from django.views.decorators.csrf import csrf_exempt
import json


def test(request):
    return JsonResponse({"Example Response": "Hello, world!"})

@csrf_exempt
def get_document(request, table, document):
    doc_ref = db.get_document(table, document)
    return JsonResponse(doc_ref)


@csrf_exempt  # Need to exempt csrf :/
def refresh_pokes(request):
    try:
        body = request.body.decode('utf-8')
        data = json.loads(body)
        uid = data['uid']
        user = db.get_user(uid)
        org_id = user['org_id']
        pokes = validators.get_unfinished_pokes(uid, org_id)
        return JsonResponse({"pokes": pokes})
    except Exception as e:
        return JsonResponse({"pokes": None, "exception": e.__class__.__name__})

@csrf_exempt
def check_poke(request):
    try:
        body = request.body.decode('utf-8')
        data = json.loads(body)
        uid = data['uid']
        poke_id = data['poke_id']
        points = validators.check_poke(uid,
                            poke_id)

        if points is not None:
            # Add the poke to the completed pokes list for the user
            db.add_complete_poke(uid, poke_id)
            return JsonResponse({"verified": True,
                                 "points": points})
        else:
            return JsonResponse({"verified": False,
                                 "points": 0})
    except Exception as e:
        return JsonResponse({"verified": False,
                             "points": 0,
                             "exception": e.__class__.__name__})


@csrf_exempt
def login(request):
    try:
        body = request.body.decode('utf-8')
        data = json.loads(body)
        uname = data['uname']
        pwd = data['pwd']
        user = auth.login_internal(uname, pwd)
        return JsonResponse({"user": user})
    except Exception as e:
        return JsonResponse({"user": None,
                             "exception": e.__class__.__name__})

@csrf_exempt
def augment_document(request, command):
    body = request.body.decode('utf-8')
    # JSON Body contains different fields for different commands, these are handled in the nested functions.
    data = json.loads(body)
    # Different cases for different objects

    def add_document(json_data):
        # Get template from table
        table = db.get_table_from_document(json_data)
        template = db.get_template_from_table(table)
        # Set fields of the template from our data
        for key in json_data:
            template[key] = json_data[key]

        id = auth.create_random_uid()
        template['id'] = id
        # Check to see if we are adding something that belongs to an organization
        if table != db.ORGS_TABLE:
            if template["org_id"] == str():
                # If our object doesn't have an org id attribute, delete it and throw an exception.
                raise TypeError
            else:
                db.add_to_organization(table, id, template['org_id'])

        # Add document to firestore
        doc_ref = db.DB.collection(table).document(template['id'])
        doc_ref.set(template)
        return template

    def delete_document(json_data):
        table = json_data["table"]
        id = json_data["document_id"]
        to_return = db.DB.collection(table).document(id).get().to_dict()
        db.DB.collection(table).document(id).delete()
        # Check if we need to also delete from org
        if table != db.ORGS_TABLE:
            db.delete_from_org(table, to_return['org_id'], id)
        return to_return

    def update_document(json_data):
        # Same exact implementation as add_document, but we don't have to create a new ID.
        # Get template from table
        table = db.get_table_from_document(json_data)
        template = db.get_template_from_table(table)
        # Set fields of the template from our data
        for key in json_data:
            template[key] = json_data[key]

        # Add document to firestore
        doc_ref = db.DB.collection(table).document(template['id'])
        doc_ref.set(template)
        return template

    try:
        response = None
        if (command == "add"):
            response = add_document(data)
        elif command == "delete":
            response = delete_document(data)
        elif command == "update":
            response = update_document(data)
        # To add a document, we only need the JSON data.
        if response is not None:
            return JsonResponse(response)
        else:
            raise TypeError
    except Exception as e:
        return JsonResponse({"exception": e.__class__})
