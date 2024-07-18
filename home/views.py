from django.shortcuts import render
from .models import Sakila

# Create your views here.
def index(request):
    # 讀取 透過 GET 傳過來的 ?id=10 資料
    id = request.GET.get("id", 1)
    country = ""
    if request.method == "POST":
    # 讀取透過 POST 傳過來的表單資料
        country = request.POST.get("country", "")
    return render(request, "home/index.html",{"id":id, 'country':country})

def countries(request):
    # 跟Model要資料
    countries = Sakila.countries()
    print(countries)

    # render()第三個參數，把資料傳給 Templates
    return render(request, "home/countries.html", {"countries": countries})

def person(request):
    return render(request, "home/person.html")

def categories(request):
    # 跟Model要資料
    categories = Sakila.categories()
    # render()第三個參數，把資料傳給 Templates
    return render(request, "home/categories.html", {"categories": categories})

def cities(request):
    id = request.GET.get('id', 1)
    country = request.GET.get('country', '')
    cities = Sakila.cities(id) 
    return render(request,"home/city.html",  {'country':country, 'cities': cities})