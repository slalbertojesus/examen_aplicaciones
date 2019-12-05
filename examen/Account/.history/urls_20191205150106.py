from django.urls import path, include
from rest_framework import routers

from .views import (
	api_detail_account_view,
	api_create_account_view,
	api_sing_up_account_view,
)

app_name = 'Account'

urlpatterns = [
	path('properties', api_detail_account_view, name="properties"),
	path('create', api_create_account_view, name="create"),
	path('login',api_sing_up_account_view, name="login"),
]