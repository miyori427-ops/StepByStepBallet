from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import User # type: ignore


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "account_id",
            "email",
            "first_name",
            "last_name",
            "birth_date",

        )

        widgets = {
            'account_id': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
        }

# ログインフォームを追加
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('Account_id', 'Password')
        widgets = {
            'Account_id': forms.TextInput(attrs={'class': 'form-control'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    