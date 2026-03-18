import time
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import empform,DocumentForm
from .models import Document, Employee, StudentProfile,User,Student
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DeleteView,UpdateView
from django.urls import reverse_lazy

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def hello(request):
    hai="<h1>welcome to django</h1>"
    return HttpResponse(hai)
def welco(request,age):
    name="steffin"
    t=17
    print("my age is",age)
    return render(request,'welcome.html',{'details':name,"t":time,'a':age})

    ## now adding a static HTML page
    # return render(request, "initial.html", {"name": "John"})
    ## now adding dynamic HTML page
    # n=input("Enter your name: ")
    # t=int(input("Enter time in hours: "))
    # return render(request, "initial.html", {"name":n,"time":t})

def emp_frm(request):
    frm=empform()
    return render(request, "regEmp.html",{"form":frm})

def Empreg(request):
    if request.method=="POST":
        frm = empform(request.POST)              #extra i code here
        if frm.is_valid():
            frm.save()
            print("......................")
            return HttpResponse("Successfully Registered")
        else:
            return HttpResponse("Error Occurred")
    else:
        print("//////////////////////")
        frm=empform()
        return render(request, "regEmp.html",{"form":frm})  
    
    
def mystatic(request):
    return render(request, "mystatic.html") 
def myhome(request):
    return render(request, "home.html")


def emp_list(request):
    emps=Employee.objects.all()
    return render(request, "listEmp.html",{"emps":emps})
       
def emp_del(request,gg):
    # print("Primary Key is:",gg)
    emp= Employee.objects.get(id=gg)
    emp.delete()
    # return HttpResponse("Deleted Successfully")
    return redirect('/listEmp')

def emp_upd(request,i):
    data=get_object_or_404(Employee,id=i)
    frm=empform(instance=data)
    return render(request, 'edit_emp.html',{'form':frm})

def emp_update(request,i):
    data=get_object_or_404(Employee,id=i)
    # frm=empform(instance=data)
    if request.method=="POST":
        frm=empform(request.POST,instance=data)
        if frm.is_valid():
            frm.save()
            return redirect('/listEmp')
    return HttpResponse("Updated Employee")

def stud_reg(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        eml=request.POST.get('email')
        FName=request.POST.get('fname')
        LName=request.POST.get('lname')
        Num=request.POST.get('ph')
        Add=request.POST.get('address')
        
        User.objects.create_user(username=uname, password=pwd, email=eml, first_name=FName,
                                 last_name=LName, phone=Num, address=Add,is_staff=False,
                                 is_active=True,is_superuser=False)
        return HttpResponse("Student Registered Successfully")
    return render(request, 'stud_reg.html')
        
def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(username=uname, password=pwd)
        if user is not None:
            if user.is_superuser == False and user.is_staff == False: #student login
                login(request, user)
                return redirect('/student/home/')
            elif user.is_superuser==True and user.is_staff==True: #teacher login
                login(request, user)
                return HttpResponse("Admin Login Successful")
        else:
            return HttpResponse("Invalid Credentials, try again")
        
    return render(request, 'login.html')

class StudentCreateView(CreateView):
    model=Student
    fields=['name','email','age']
    template_name='student_form.html'
    success_url='/studenthome/'
    
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'  # Default is 'object_list'
    
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    # success_url='/students/list/'
    success_url =reverse_lazy('student_list')   
    
class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'age']
    template_name = 'student_form_edit.html'
    success_url = reverse_lazy('student_list')  
    
            
def set_session(request):
    if request.method=="POST":
        request.session['username']=request.POST.get('username')
        request.session['password']=request.POST.get('password')
        return HttpResponse("Session Set Successfully")
    return render(request, 'set_ss.html')

def get_session(request):
    username = request.session.get('username')
    password = request.session.get('password')
    if not username and not password:
        return HttpResponse("No session data found")
    return HttpResponse(f"Username: {username} <br> Password: {password}")

def shhs(request):
    user = request.session.get('username')
    print("hello session........", user)
    return HttpResponse("Hello Session")

def delete_session(request):
    if 'username' in request.session or 'password' in request.session:
        request.session.pop('username', None)
        request.session.pop('password', None)
        return HttpResponse("Session Deleted Successfully")
    return HttpResponse("No session to delete")
    

@login_required
def logout(request):
    auth_logout(request)
    return redirect('/login/')

def reg_student_list(request):
    students_list = StudentProfile.objects.select_related('user')
    return render(request, 'reg_student_list.html', {'students': students_list})

def set_cookieeee(request):
    response=HttpResponse("Cookie id Set")
    response.set_cookie('name','arun',max_age=3600)## name->cookie name , arun->cookie value , max_age->cookie lifetime in seconds
    response.set_cookie('age',22)
    response.set_cookie('place','kochi')
    return response

def get_cookieeee(request):
    name=request.COOKIES('name')
    age=request.COOKIES('age')
    # place=request.COOKIES('place')
    place=request.COOKIES.get('place','not found')
    return HttpResponse(f"Name:{name} <br> Age:{age} <br> Place:{place}")

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("File uploaded successfully")
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})

def list_files(request):
    files=Document.objects.all()
    return render(request,'listdata.html',{'data':files})


def send_eml(request):
    send_mail(
        subject="Welcome to django",
        message="My first email",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['stefinjames1@gmail.com'],
        fail_silently=False
    )
    return HttpResponse("Email Sent Successfully")
    
      