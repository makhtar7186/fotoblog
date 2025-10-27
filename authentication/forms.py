from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Nom d'utilisateur")
    password = forms.CharField(max_length=128, label="Mot de passe", widget=forms.PasswordInput)