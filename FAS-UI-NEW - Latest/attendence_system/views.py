from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.contrib import messages
from .forms import LoginForm
from attendence_system.models import employee

from django.urls import reverse 
from django.contrib.auth.models import User,auth

#from attendence_system.facedetector import FaceDetector
#from attendence_system.facerecognizer import FaceRecognizer
#from facedetector import FaceDetector
#from facerecognizer import FaceRecognizer
import csv
import os
import pandas as pd
from pathlib import Path
from .gather_selfies import gather_selfies
from .recognize import recognize


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    # login(request, user)
                    # return HttpResponse('Authenticated '\
                    #                     'successfully')
                    context = {}
                    return render(request, 'attendence_system/home2.html', context)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'attendence_system/registration/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'attendence_system/dashboard.html',
                  {'section': 'dashboard'})
@login_required
def home(request):
    return render(request, 'attendence_system/home2.html', {'section': 'home'})




def record_attn(request):
    return render(request, 'attendence_system/record_attendence.html', {'section': 'record_attn'})


@login_required
def attn_records(request):
    BasePath = Path(__file__).resolve(strict=True).parent
    # print(path)
    o_path1 = os.path.join('output', 'Employee_Database.csv')  # newp)
    output_path1 = os.path.join(BasePath, o_path1)  # newp)
    employee_df = pd.read_csv(output_path1, names=["emp_id", "first_name", "last_name", "email_id"])
    employee_df = employee_df.applymap(str)
    print(employee_df)

    return render(request, 'attendence_system/attn_records.html', {'section': 'attn_records'})



@login_required
def register_user(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'%s Username Taken'%username)
                return redirect ("register_user")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'EmailID already used'%email)
                return redirect ("register_user")
            else:

                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save
                if user.save:
                    messages.success(request,' %s registered succesfully '%username)
                return redirect('register_user')
        else:
            messages.info(request,'Password Not Matching')
            return redirect ("register_user")
    else:
        return render(request, 'attendence_system/register.html',  {'section': 'register_user'})

@login_required
def register_employee(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        employee_id=request.POST['employee_id']
        email_id=request.POST['email_id']

        BasePath = Path(__file__).resolve(strict=True).parent
        # print(path)
        o_path1 = os.path.join('output', 'Employee_Database.csv')  # newp)
        output_path1 = os.path.join(BasePath, o_path1)  # newp)
       
        # if employee.filter(employee_id=employee_id).exists():
        #     messages.error(request,'%s Username Taken'%employee_id)
        #     return redirect ("register_employee")
        # elif employee.filter(email_id=email_id).exists():
        #     messages.info(request,'%s EmailID already used'%email_id)
        #     return redirect ("register_employee")
        # else:

        emp=employee(employee_id=employee_id,email_id=email_id,first_name=first_name,last_name=last_name)

        #gather_selfies(employee_id)

        employee_df = pd.read_csv(output_path1, names=["emp_id", "first_name", "last_name", "email_id"])
        employee_df = employee_df.applymap(str)

        if employee_df[employee_df['emp_id'].str.contains(str(employee_id))]['emp_id'].any():
            messages.error(request,' %s employee already Exists'%employee_id)
            return redirect('register_employee')
        else:
            emp.save

        #save

        if emp.save:
            messages.success(request,' %s employee  successfully created  '%employee_id)
            with open(output_path1,"a+") as file:
                writer=csv.writer(file)
                writer.writerow([employee_id, first_name, last_name, email_id])
            gather_selfies(employee_id)
        return redirect('register_employee')
      
    else:
        return render(request, 'attendence_system/register_emp.html',  {'section': 'register_employee'})

"""
def gather(request):
    if request.method == 'POST':
        employee_id=request.POST['employee_id']
    employee_id = employee_id
    gather_selfies(employee_id)

"""

def recognize1(request):
    prediction=recognize()
    if prediction=='Unknown':
        messages.error(request,"Unauthorized Entry ")
    else:
        messages.success(request,"%s  has recorded attendance succesfully  "%prediction)

    return redirect("record_attn")