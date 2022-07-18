from django import forms

class OperationForm(forms.Form):
    num1 = forms.IntegerField(label="Enter number 1")         #Creating form input field
    num2 = forms.IntegerField(label="Enter number 2")         #Creating form input field
    def clean(self):                    #This clean method overriding method in BaseForm
        cleaned_data = super().clean()   #super() -> For going to parent class. clean() -> Method defined in Baseform
        n1 = cleaned_data.get("num1")    #Taking the values from input field
        n2 = cleaned_data.get("num2")    #Taking the values from input field
        if n1 < 0 :               #Validating
            msg = "Invalid number"
            self.add_error("num1",msg)   #Using add_error() sending message if validation false.First argument is field,and
        if n2 < 0 :                      #second one is message.
            msg = "Invalid number"
            self.add_error("num2",msg)
