from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
        
    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('password_confirm'):
            raise forms.ValidationError('As senhas não conferem')
        return data        
    
    
    
    