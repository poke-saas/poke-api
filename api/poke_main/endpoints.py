from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    # Sanity check testing endpoint
    path("test/", views.test, name='test'),

    # Picking up where cloud functions left off
    path("get/<str:table>/<str:document>", views.get_document, name="Get Document")
]