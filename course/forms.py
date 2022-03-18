import email
from django import forms


class CustomPaymentForm(forms.Form):
    Total_course = forms.IntegerField()
    TotalCredit = forms.CharField(max_length=50)
    TotalFees = forms.CharField(max_length=50)
    email = forms.EmailField()