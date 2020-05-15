from django.shortcuts import render
from django.http import JsonResponse
from .utils import db_entry as db
from .social_media import validators, twitter
from flask import jsonify
from django.views.decorators.csrf import csrf_exempt
import json


def test(request):
    return JsonResponse({"Example Response": "Hello, world!"})


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
