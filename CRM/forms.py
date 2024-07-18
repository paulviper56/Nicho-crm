from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email address'}))
    firstname =forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    surname = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    
    class meta:
        model = User
        fields =('email','firstname','surname','username','password1','password2')

        def __init__(self, *args,**kwargs):
            super(SignupForm,self).__init__(*args,**kwargs)

            self.fields['username'].widget.atrrs['class']='form-control'
            self.fields['username'].widget.atrrs['placeholder']='username'
            self.fields['username'].label = ""
            self.fields['username'].max_length = 20

            self.fields['password1'].widget.atrrs['class']='form-control'
            self.fields['username'].widget.atrrs['placeholder']='Enter password'
            self.fields['username'].label = ""
            self.fields['username'].max_length = 50

            self.fields['username'].widget.atrrs['class']='form-control'
            self.fields['username'].widget.atrrs['placeholder']='Confirm password'
            self.fields['username'].label = ""
            self.fields['username'].max_length = 50
