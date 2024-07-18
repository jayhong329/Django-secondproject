from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('countries/', views.countries),
    path('about/', views.about),    #http://127.0.0.1:8000/about/
    path('about/<int:year>', views.about),   #http://127.0.0.1:8000/about/2012
    path('person/', views.person),  #http://127.0.0.1:8000/person/
    path('categories/', views.categories),  #http://127.0.0.1:8000/categories/
    path('cities/', views.cities),  #http://127.0.0.1:8000/cities/
]