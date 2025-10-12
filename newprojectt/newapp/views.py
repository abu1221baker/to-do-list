from django.shortcuts import render,redirect
from .models import Data
from django.contrib.auth.models import User
from  django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    if request.method == "POST":
        data = request.POST
        task = data.get("task")
        Data.objects.create(
            task=task
        )
    querryset = Data.objects.all()
    if request.GET.get("q"):
        querryset = querryset.filter(task__icontains = request.GET.get("q"))
    context={"context":querryset}
    return render(request,"index.html",context)

def register(request):
    if request.method == "POST":
        data=request.POST
        username= data.get("username")
        first_name= data.get("first_name")
        last_name=data.get("last_name")
        password=data.get("password")
        email=data.get("email")

        if User.objects.filter(username=username).exists():
            messages.error(request,"this username already  exits")

        elif User.objects.filter(email=email).exists():
            messages.error(request,"this email already exits")
        else:
            User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            return redirect("sign") 
    return render(request,"register.html")

def sign(request):
    if request.method == "POST":
        data= request.POST
        username=data.get("username")
        password = data.get("password")
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.error(request,"incorect username or password")
        
            
    return render(request,"sign.html")

def logout_func(request):
    logout(request)
    return redirect("sign")

def delete_task(request,id):
    querryset=Data.objects.get(id=id)
    querryset.delete()
    return redirect("home")

def update_task(request,id):
    querryset = Data.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        task = data.get("task")

        querryset.task=task
        querryset.save()
        return redirect("home")
    context = {"context":querryset }

    return render(request,"update.html",context)