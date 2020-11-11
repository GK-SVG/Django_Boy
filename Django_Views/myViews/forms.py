from django import forms

class Contact(forms.Form):
    Mobile_No = forms.CharField(max_length=10)