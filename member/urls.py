from django.urls import path
from member import views

urlpatterns = [
    path('', views.index),  #http://127.0.0.1:8000/member/
    path('member/register', views.register),  #http://127.0.0.1:8000/member/register
]