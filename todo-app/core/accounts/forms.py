from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class UserLogoutForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()