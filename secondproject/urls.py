"""
URL configuration for secondproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from member import views as membviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index),  #http://127.0.0.1:8000/home/
    path('countries/', views.countries),  #http://127.0.0.1:8000/countries/
    path('person/', views.person),  #http://127.0.0.1:8000/person/
    path('categories/', views.categories),  #http://127.0.0.1:8000/categories/
    path('member/', membviews.register),  #http://127.0.0.1:8000/member/
    path('cities/', views.cities),  #http://127.0.0.1:8000/cities/
    path('member/register', membviews.register),  #http://127.0.0.1:8000/member/register
]
