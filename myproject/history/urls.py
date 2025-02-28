# myproject/urls.py
from django.contrib import admin
from django.urls import path
from . import views  # 同じディレクトリにあるviews.pyをインポート

urlpatterns = [
    path('c17/', views.c17, name='c17'),
    path('c19/', views.c19, name='c19'),
    path('cmodern/', views.cmodern, name='cmodern'),
    path('historyindex/', views.historyindex, name='historyindex'),
    path('c14/', views.c14, name='c14'),
    path('c16/', views.c16, name='c16'),
]