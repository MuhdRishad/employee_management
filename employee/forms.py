from django import forms
from employee.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#
# class EmployeeCreateForm(forms.Form):
#     emp_name = forms.CharField(label="Name",widget=forms.TextInput(attrs={"class":"form-control form-control-sm"}))
#     emp_email = forms.EmailField(label="E-Mail",widget=forms.EmailInput(attrs={"class":"form-control form-control-sm"}))
#     emp_designation = forms.CharField(label="Designation",widget=forms.TextInput(attrs={"class":"form-control form-control-sm"}))
#     emp_experience = forms.IntegerField(label="Experience",widget=forms.NumberInput(attrs={"class":"form-control form-control-sm"}))
#     emp_salary = forms.IntegerField(label="Salary",widget=forms.NumberInput(attrs={"class":"form-control form-control-sm"}))
#     def clean(self):
#         cleaned_data = super().clean()
#         experience = cleaned_data.get("emp_experience")
#         if experience < 0 :
#             msg = "Negtive not allowed"
#             self.add_error("emp_experience",msg)



#  Form create using ModelForm
class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            "emp_name":forms.TextInput(attrs={"class":"form-control "}),
            "emp_email":forms.EmailInput(attrs={"class":"form-control "}),
            "emp_designation":forms.TextInput(attrs={"class":"form-control "}),
            "emp_experience" :forms.NumberInput(attrs={"class": "form-control "}),
            "emp_salary":forms.NumberInput(attrs={"class": "form-control "}),
            "emp_place": forms.TextInput(attrs={"class": "form-control "}),
        }

class UserResgistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        ]

class UserLogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())