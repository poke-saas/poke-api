from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    # Sanity check testing endpoint
    path("test/", views.test, name='test'),

    # Picking up where cloud functions left off
    # TODO: Make seperate Django apps for each base (firestore, services, auth)
    # Firestore paths
    path("firestore/get/<str:table>/<str:document>", views.get_document, name="Get Document")
]