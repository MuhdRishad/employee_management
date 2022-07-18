from django.shortcuts import render
from django.views.generic import View
from mathfunctions.forms import *
from django.contrib import messages

# Create your views here.

                    # HOME PAGE

class HomeView(View):
    def get(self,request):
        return render(request,"math-home.html")

                    # ADDITION PAGE
class AdditionView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"math-add.html",{"form":form})
    def post(self,request):
        form = OperationForm(request.POST)
        if not form.is_valid():
            messages.error(request,"Failed to add")
            return render(request,"math-add.html",{"form":form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        result = n1 + n2
        messages.success(request,"Successfully added")
        return render(request,"math-add.html",{"add":result,"form":form})


                    # SUBSTRACTION PAGE
class SubstractionView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"math-substraction.html",{"form":form})
    def post(self,request):
        form = OperationForm(request.POST)
        if not form.is_valid():
            messages.error(request,"Failed to substract")
            return render(request,"math-substraction.html",{"form":form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        result = n1 - n2
        messages.success(request,"successfully substracted")
        return render(request,"math-substraction.html",{"sub":result,"form":form})


                    # MULTIPLICATION PAGE
class MultiplicationView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"math-multiplication.html",{"form":form})
    def post(self,request):
        form = OperationForm(request.POST)
        if not form.is_valid():
            messages.error(request,"Failed multiply")
            return render(request,"math-multiplication.html",{"form":form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        result = n1 * n2
        messages.success(request,"Successfully multiplyed")
        return render(request,"math-multiplication.html",{"multi":result,"form":form})

                    #DIVISION PAGE
class DivisionView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"math-division.html",{"form":form})
    def post(self,request):
        form = OperationForm(request.POST)
        if not form.is_valid():
            messages.error(request,"Failed dividing")
            return render(request,"math-division.html",{"form":form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        result = n1 / n2
        messages.success(request,"Successfully devided")
        return render(request,"math-division.html",{"div":result , "form":form})