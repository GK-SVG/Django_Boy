from django import forms
from .models import Code

class CodeForm(forms.ModelForm):
    code = forms.CharField(label='Code',help_text='Enter OTP')
    class Meta:
        model = Code
        fields = ('code',)