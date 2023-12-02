from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("delete_recipe/<int:id>/", views.delete_recipe, name="delete_recipe"),
]
