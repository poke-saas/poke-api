from django.shortcuts import render
from django.http import JsonResponse
from .utils import db_entry

# Create your views here.


def test(request):
    return JsonResponse({"Example Response": "Hello, world!"})

def get_document(request, table, document):
    doc_ref = db_entry.get_document(table, document)
    return JsonResponse(doc_ref)