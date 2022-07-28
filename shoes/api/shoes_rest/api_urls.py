from django.urls import path

from .views import api_list_shoes

urlpatterns = [
    path("shoes_rest/", api_list_shoes, name="api_list_shoes"),
]