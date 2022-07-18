# from django.shortcuts import render,redirect
# from django.views.generic import View
# from django.http import HttpResponse
# from employee.forms import *
# from django.contrib import messages
#
#
#
#
#
# #EMPLOYEE ADDING PAGE
# class EmployeeCreateView(View):
#     form_class = EmployeeForm
#     template_name = "emp-add.html"
#
#     def get(self,request):
#         form = self.form_class()
#         return render(request,self.template_name,{"form":form})
#
#     def post(self,request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data.get("emp_id"))
#             print(form.cleaned_data.get("emp_name"))
#             print(form.cleaned_data.get("emp_email"))
#             print(form.cleaned_data.get("emp_designation"))
#             print(form.cleaned_data.get("emp_experience"))
#             print(form.cleaned_data.get("emp_salary"))
#
#             messages.success(request,"Profile added successfully")
#             return redirect("emp_add")
#         else:
#             messages.error(request,"Profile adding failed")
#             return render(request,self.template_name,{"form":form})

from django.shortcuts import render,redirect
from employee.models import Employee
from django.contrib import messages
from django.views.generic import View
from employee.forms import EmployeeCreateForm,UserResgistrationForm,UserLogInForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

def signin_required(fun):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fun(request,*args,**kwargs)
        else:
            messages.error(request,"Please login")
            return redirect("sign-in")
    return wrapper

@method_decorator(signin_required,name="dispatch")
class EmployeeCreateView(View):
    form_class = EmployeeCreateForm
    template_name = "emp-add.html"

    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # Employee.objects.create(
            #     emp_name=form.cleaned_data.get("emp_name"),
            #     emp_email=form.cleaned_data.get("emp_email"),
            #     emp_designation=form.cleaned_data.get("emp_designation"),
            #     emp_experience=form.cleaned_data.get("emp_experience"),
            #     emp_salary=form.cleaned_data.get("emp_salary"),
            # )
            messages.success(request,"Employee added succesfully")
            return redirect("emp-add")
        else:
            messages.error(request,"Employee adding failed")
            return render(request, self.template_name, {"form": form})

@method_decorator(signin_required,name="dispatch")
class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        return render(request,"emp-list.html",{"employees":qs})

@method_decorator(signin_required,name="dispatch")
class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        #kwargs= {eid:12}
        emp_id = kwargs.get("eid")
        qs = Employee.objects.get(id=emp_id)
        return render(request,"emp-detail.html",{"employee":qs})

@method_decorator(signin_required,name="dispatch")
class EmployeeEditView(View):
    def get(self,request,*args,**kwargs):
        eid = kwargs.get("eid")
        employee = Employee.objects.get(id=eid)
        form = EmployeeCreateForm(instance=employee)
        return render(request,"emp-edit.html",{'form':form,"qs":employee})
    def post(self,request,*args,**kwargs):
        eid = kwargs.get("eid")
        employee = Employee.objects.get(id=eid)
        form = EmployeeCreateForm(request.POST,files=request.FILES,instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated succesfully")
            return redirect("emp-list")
        else:
            messages.error(request, "Employee update failed")
            return render(request, "emp-edit.html", {"form": form})

@signin_required
def remove_employee(request,*args,**kwargs):
    eid = kwargs.get("eid")
    employee = Employee.objects.get(id=eid)
    employee.delete()
    messages.success(request, "Employee deleted succesfully")
    return redirect("emp-list")


def index(request):
    return render(request,"base.html")

class SignUpView(View):
    template_name = "registration.html"
    form_class = UserResgistrationForm

    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account has been created successfully")
            return redirect("sign-in")
        else:
            messages.error(request,"Account creation failed")
            return render(request,self.template_name,{"form":form})


class UserLogInView(View):
    form_class = UserLogInForm
    template_name = "login.html"

    def get(self,request,*args,**kwargs):
        form = self.form_class()
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect("index")
            else:
                messages.error(request,"Invalid username or password")
                return render(request, self.template_name, {"form": form})

@signin_required
def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("sign-in")