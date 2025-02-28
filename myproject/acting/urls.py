# myproject/urls.py
from django.contrib import admin
from django.urls import path
from . import views  # 同じディレクトリにあるviews.pyをインポート

urlpatterns = [
    path('acting/', views.acting, name='acting'),
    path('featuring/', views.featuring, name='featuring'),
]