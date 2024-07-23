from django.urls import path
from myapp import views

urlpatterns = [
    # path('比對路徑')
    path('', views.index),  #http://127.0.0.1:8000/store/
]