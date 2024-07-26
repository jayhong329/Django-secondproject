from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    title = '我的商店 首頁'
    now = datetime.now()
    id = '123e4567-e89b-12d3-a456-426655440000'
    value1 = ['aaa',['bbb',['eee','fff'],'ccc']]
    value2 =[
    {"name": "zed", "age": 19},
    {"name": "amy", "age": 22},
    {"name": "joe", "age": 31},
    ]

    return render(request, 'myapp/index.html', locals())



    # return HttpResponse('<h2>我的APP 首頁</h2>')

def details(request, producr_id=''):
    return HttpResponse('<h2>讀出商品編號 {producr_id}的商品</h2>')

def about(request, year= datetime.now().year):
    return HttpResponse(f'<h2> ABOUT {year} </h2>')

# publisg => 2024/07/23
def blog(request, publish = None):
    return HttpResponse(f'<h2>讀取 {publish} 的文章 </h2>')