from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator 
# from django.contrib.auth import get_user_model
from vege.seed import *
# User=get_user_model()

def home(request):
    


    return render(request,"login.html")
@login_required(login_url="/login/")
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


@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
def delete_receipe(request,id):
    # print(id)
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect( '/receipes/')

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists:
            messages.error(request,'invalid username please enter correct username')
            return redirect('/login/')
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'invalid password')
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('/receipes/')



    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect('/login/') 


def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'username already taken')
            return redirect('/register')
        

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
          
        )
        user.set_password(password)
        user.save()
        messages.info(request,'accound created successfully')
        return redirect('/login')
    return render(request,"register.html")

from django.db.models import Q,Sum,Avg,Max,Min


def get_students(request):
    # queryset=Student.objects.all()
    queryset=Student.objects.all().order_by("studentreportcard__student_rank")
    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(
            Q(student_name__icontains=search)|
            Q(student_id__student_id__icontains=search)|
            Q(department__department__icontains=search)|
            Q(student_email__icontains=search)|
            Q(student_age__icontains=search)

            )
    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    # print(page_obj)
    # print(page_obj.object_list)
    # print(page_obj.has_next())
    return render(request,"report/student.html",{'queryset':page_obj})

from .seed import generate_report_card
def see_marks(request,student_id):
    # generate_report_card()
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    totalmarks=queryset.aggregate(totalmarks=Sum('marks'))
    avgg=queryset.aggregate(avgg=Avg('marks'))
    maxval=queryset.aggregate(maxval=Max('marks'))
    minval=queryset.aggregate(minval=Min('marks'))
    # current_rank=-1
    # ranks=Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
    # # print(rank)
    # i=1
    # for rank in ranks:
    #     # print(rank.student_id)
    #     if student_id==rank.student_id.student_id:
    #         current_rank=i
    #         break
    #     i=i+1
    # # print(totalmarks)
    return render(request,"report/see_marks.html",{'queryset':queryset, 'totalmarks':totalmarks,'avgg':avgg,'maxval':maxval,'minval':minval})