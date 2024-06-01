# forms.py
from django import forms
from home.models import Customer

class Table1Form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'age', 'gender', 'address', 'password']
        widgets = {
            'userpassword': forms.PasswordInput(attrs={'size': 30}),  # Adjust size as needed
        }
