from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,Contact

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields  = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('Organization','profile_pic')

class Contact(forms.ModelForm):
    class Meta():
        model = Contact
        fields = ('Name','Email','Organization','Message')
        widgets = {
        'Name':forms.TextInput(attrs={'class':'form-control'}),
        'Email':forms.EmailInput(attrs={'class':'form-control'}),
        'Organization':forms.TextInput(attrs={'class':'form-control'}),
        'Message':forms.TextInput(attrs={'class':'form-control'})

        }



        
        

        
         
         


