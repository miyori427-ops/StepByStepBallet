
# primary/urls.py
from django.urls import path
from . import views  # viewsをインポート

app_name = 'primary'

urlpatterns = [
    path('first/', views.first, name='first'),
]

