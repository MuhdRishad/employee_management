from django.shortcuts import render
from django.views.generic import View,TemplateView
from calculator.forms import OperationForm

# Create your views here.
                                #HOME PAGE

class HomeView(View):
    def get(self,request):
        return render(request,"calc_home.html")

                                #ADD PAGE

class AddView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,'add.html',{"form":form})
    def post(self,request):
        form = OperationForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get("num1")
            n2 = form.cleaned_data.get("num2")
            result = n1 + n2
            return render(request,"add.html",{"addres":result,"form":form})
        else:
            return render(request,"add.html",{"form":form})

                                #SUBSTRACTION PAGE

class SubView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"sub.html",{"form":form})
    def post(self,request):
        # n1 = request.POST.get('num1')
        # n2 = request.POST.get('num2')
        # result = int(n1) - int(n2)
        # return render(request,"sub.html",{"subres":result})

        form = OperationForm(request.POST)
        if not form.is_valid():
            return render(request,"sub.html",{"form":form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        result = n1 - n2
        return render(request,"sub.html",{"subres":result , "form":form})


                                #MULTIPLICATION PAGE

class MultyView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"multiplication.html",{"form":form})
    def post(self,request):
        form = OperationForm(request.POST)
        if not form.is_valid():
            return render(request,"multiplication.html",{"form":form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        result = n1 * n2
        return render(request,"multiplication.html",{"mulres":result,"form":form})

                                #DIVISION PAGE

class DivisionView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"division.html",{"form":form})
    def post(self,request):
        form = OperationForm(request.POST)
        if not form.is_valid():
            return render(request,"division.html",{"form":form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        result = n1 / n2
        return render(request,"division.html",{"divres":result,"form":form})

                                #EXPONENSATION PAGE

class ExpView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"exponent.html",{"form":form})
    def post(self,request):
        form = OperationForm(request.POST)
        if not form.is_valid():
            return render(request, "exponent.html", {"form":form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        result = n1 ** n2
        return render(request,"exponent.html",{"expres":result,"form":form})

                                #MODULUS PAGE

class ModView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"modules.html",{"form":form})
    def post(self,request):
        form = OperationForm(request.POST)
        if not form.is_valid():
            return render(request, "modules.html", {"form": form})
        n1 = form.cleaned_data.get("num1")
        n2 = form.cleaned_data.get("num2")
        result = n1 % n2
        return render(request,"modules.html",{"modres":result,"form":form})

                                #FACTORIAL PAGE

class FactView(View):
    def get(self,request):
        return render(request,"factorial.html")
    def post(self,request):
        num = request.POST.get("num")
        fact = int(num)
        factorial = 1
        for i in range(1,fact+1):
            factorial = factorial * i
        return render(request,"factorial.html",{"factres":factorial})

                                #WORDCOUNT PAGE

class WordCountView(View):
    def get(self,request):
        return render(request,"wordcount.html")
    def post(self,request):
        word = request.POST.get("wordcount")
        words = word.split(" ")
        wc = {}
        for w in words:
            if w not in wc:
                wc[w] = 1
            else:
                wc[w] += 1
        for k,v in wc.items():
            pass
            # print(k,v)
        return render(request,"wordcount.html",{"wordres":wc})

                                #PRIME NUMBER USING DICTIONARY
#
# class PrimeNumberView(View):
#     def get(self,request):
#         return render(request,"primenumber.html")
#     def post(self,request):
#         initial = request.POST.get("initial")
#         final = request.POST.get("final")
#         prime = {}
#         for i in range(int(initial),int(final)):
#             for j in range(2,i):
#                 if i % j == 0:
#                     break
#             else:
#                 prime[i] = "Prime Number"
#         for k,v in prime.items():
#             pass
#         return render(request,"primenumber.html",{"primeres":prime})

                                #PRIME NUMBER USING LIST

class PrimeNumberView(View):
    def get(self,request):
        return render(request,"primenumber.html")
    def post(self,request):
        initial = request.POST.get("initial")
        final = request.POST.get("final")
        prime = []
        for i in range(int(initial),int(final)):
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                prime.append(i)
        return render(request,"primenumber.html",{"primeres":prime})

