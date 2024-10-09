from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="indexKeyboard"),
    path("shortcut", views.shortcut, name="shortcut"),
    path("specs", views.specs, name="specs"),
]