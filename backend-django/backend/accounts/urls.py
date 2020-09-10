from django.urls import path, include
from . import views


app_name = 'accounts'

urlpatterns = [
  path('', views.user),
  path('send/<str:email>', views.email),
]

