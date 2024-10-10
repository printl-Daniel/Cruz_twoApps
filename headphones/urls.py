from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="indexHeadphones"),
    path("topbrands", views.brands, name="topbrands"),
    path("specsHeadPhones", views.specs, name="specsHeadphones"),
]