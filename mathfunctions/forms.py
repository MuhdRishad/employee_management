from django import forms

class OperationForm(forms.Form):
    num1 = forms.IntegerField(label="Enter number",widget=forms.NumberInput(attrs={"class":"form-control form-control-sm"}))
    num2 = forms.IntegerField(label="Enter number",widget=forms.NumberInput(attrs={"class":"form-control form-control-sm"}))
    def clean(self):
        cleaned_data = super().clean()
        n1 = cleaned_data.get("num1")
        n2 = cleaned_data.get("num2")
        if n1 < 0 :
            msg = "Negative values not allowed"
            self.add_error("num1",msg)
        if n2 < 0 :
            msg = "Negative values not allowed"
            self.add_error("num2",msg)
