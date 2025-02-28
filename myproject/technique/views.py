from venv import logger
from django.shortcuts import render, redirect
from django.urls import reverse
#from myproject.technique.forms import AccountAddForm
from django import forms
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class AccountAddForm(forms.Form):
    # Define your form fields here
    username = forms.CharField(max_length=150, required=True, label='Username')
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')

from django.apps import AppConfig

class TechniqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myproject.technique'

# Create your views here

def indexa(request):


    my_list = [
        ["1", "HlGFzHE3W50.jpg", "https://www.youtube.com/watch?v=HlGFzHE3W50"],
        ["2", "lhvGiY0Qjt8.jpg", "https://www.youtube.com/watch?v=lhvGiY0Qjt8"],
        ["3", "YB0rrc5B2LM.jpg", "https://www.youtube.com/watch?v=YB0rrc5B2LM"],
        ["4", "WjbJReewZC4.jpg", "https://www.youtube.com/watch?v=WjbJReewZC4"],
        ["5", "vprWhBtb298.jpg", "https://www.youtube.com/watch?v=vprWhBtb298"],
        ["6", "NOHArqrTk40.jpg", "https://www.youtube.com/watch?v=NOHArqrTk40"],
        ["7", "gqAcBxaowEw.jpg", "https://www.youtube.com/watch?v=gqAcBxaowEw"],
        ["8", "pasdesbourres.jpg", "https://www.youtube.com/watch?v=1hdHc1hJAWU"]
    ]

    return render(request, "indexa.html", {
        "movies": my_list
    })

def indexb(request):
    return render(request, "indexb.html")

#def indexb(request, id):
    # id 引数を使って何かをする
    return render(request, 'indexb.html', {'indexb_id': id})



def indexmove(request):
    # id 引数を使って何かをする
    return render(request, 'indexmove.html')

def index2(request):
    return render(request, "index2.html")

def home(request):
    return render(request, "home.html")


def signup(request):
    return render(request, "signup.html")

class TechniqueIndexView(TemplateView):
    """Techniqueアプリのホームページビュー"""
    template_name = "technique/indexa.html"