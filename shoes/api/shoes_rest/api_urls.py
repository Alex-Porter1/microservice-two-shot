from django.urls import path

from .views import api_list_shoes,  api_delete_shoes

urlpatterns = [
    path("shoes_rest/", api_list_shoes, name="api_list_shoes"),
    path("shoes_rest/<int:pk>/", api_delete_shoes, name="api_delete_shoes"),
]