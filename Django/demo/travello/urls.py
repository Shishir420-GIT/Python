from django.urls import path
from . import views

urlpatterns = [
    path('travello', views.travello)
]