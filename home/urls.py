from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("delete_recipe/<int:id>/", views.delete_recipe, name="delete_recipe"),
    path("update_recipe/<int:id>/", views.update_recipe, name="update_recipe"),
]
