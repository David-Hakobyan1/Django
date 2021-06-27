from django import forms

class CalcForm(forms.Form):
    first_number = forms.CharField(label='First number:', max_length=100)
    symbol = forms.CharField(label='Symbol:', max_length=100)
    secound_number = forms.CharField(label='Secound number:', max_length=100)
