from django.shortcuts import render
from .models import user,file_details,file_file
from django.http import HttpResponse
import socket
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request,"homepage.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def register_user(request):
    name = request.POST["name"]
    userList = list(user.objects.all().filter(username=name))
    if len(userList)==0:
        user_obj = user()
        user_obj.username = request.POST["name"]
        user_obj.password = request.POST["pass1"]
        user_obj.save()
        return render(request,"register.html",{"register_sucess":"User Registration Successful"})
    else:
        print(userList)
        return render(request,"register.html",{"register_error":"Username already exists"})

def user_login(request):
    name = request.POST["name"]
    password = request.POST["pass"]
    userList = list(user.objects.all().filter(username=name))
    if len(userList)==1:
        if userList[0].password==password:
            return render(request,"upload.html",{"username":name.upper()})
    return render(request,"login.html",{"login_error":"Check username and password"})

def send_file(request):
    if request.method == 'POST':
        f = request.FILES["sent_file"]
        fs = FileSystemStorage()
        fsd = file_details()
        fsf = file_file()
        fs.save(f.name,f)
        file_path = "DOWNLOADED_FILES/"+f.name
        opened_file = open(file_path)
        file_content = opened_file.read()
        file_parts = len(file_content)//256
        tempForI=0
        for i in range(file_parts):
            tempForI = i
            print(file_content[i*256:(i+1)*256])
        print(file_content[(tempForI+1)*256:])

    return HttpResponse("Done")