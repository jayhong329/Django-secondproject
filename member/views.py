from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
# def index(request):
#     return render(request, "member/index.html")

def index(request):

    # html = '<h2>Hello Django</h2>'
    
    # print(request.headers)
    # 讀出 headers 裡面的某類型資料
    # print(request.headers.get('Content-Type'))
    # print(request.headers.get('User-Agent'))

    # 讀出 hearders 中的所有資料
    # html += '<ul>'
    # for key, value in request.hearders.item():
    #     html += f'<li>{key}:{value}</li>'
    # html += '</ul>'

    # 讀取透過GET傳過來的資料 ?key=value
    name = request.GET.get('username') # 讀不到username 回傳 none
    if name != None :
        name = "Django"
    html = f'<h2>Hello {name} </h2>'
    return HttpResponse(html)

def register(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        avator = request.FILES.get('userphoto')
        file_name = avator.name
        file_size = avator.size
        file_type = avator.content_type
        # print(name)
        # print(email)
        # print(avator)

        print(f"檔案名稱:{file_name}")
        print(f"檔案大小:{file_size}")
        print(f"檔案類型:{file_type}")

        # 上傳檔案
        fs = FileSystemStorage()
        upload_file = fs.save(file_name, avator)
        print(f"uploads file:{upload_file}")


    return render(request, 'member/register.html',)

