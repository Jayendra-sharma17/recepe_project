from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User
def receipes(request):
    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        print(receipe_description)
        print(receipe_name)
        print(receipe_image)
        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
        )
        return redirect('/receipes/')

    queryset=Receipe.objects.all()

    if request.GET.get('search'):
        # print(request.GET.get('search'))
        queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))
    context={'receipes':queryset}
    
    
    return render(request,'receipes.html',context)

def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)

    if request.method=="POST":
        data=request.POST

        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description

        if receipe_image:
            queryset.receipe_image=receipe_image

        queryset.save()    

        return redirect('/receipes/')
        
    context={'receipe':queryset}
    return render(request,'update_receipes.html',context)

def delete_receipe(request,id):
    # print(id)
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect( '/receipes/')

def login_page(request):
    
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
          
        )
        user.set_password(password)
        user.save()
        return redirect('/register')
    return render(request,"register.html")