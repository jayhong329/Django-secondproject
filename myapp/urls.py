from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    # path('比對路徑', '要執行的function')
    path('', views.index, name='index'),  #http://127.0.0.1:8000/store/
    path('details/<uuid:product_id>', views.details),
    path('about/', views.about, name = 'about'),  #http://127.0.0.1:8000/store/about/
    path('about/<int:year>', views.about),
    path('blog/<path:publish>', views.blog),
    path ('show', views.show, name= 'show')
]