from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="indexHeadphone"),
    path("topbrands", views.brands, name="topbrands"),
    path("specs", views.specs, name="specsHeadphone"),
]