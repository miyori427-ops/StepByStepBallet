# myproject/urls.py
from django.contrib import admin
from django.urls import path
from . import views  # 同じディレクトリにあるviews.pyをインポート


urlpatterns = [
    path('aurora/', views.aurora, name='aurora'),
    path('blackswan/', views.blackswan, name='blackswan'),
    path('Cinderella/', views.Cinderella, name='Cinderella'),
    path('gayane/', views.gayane, name='gayane'),
    path('Kaizoku/', views.Kaizoku, name='Kaizoku'),
    path('Paris/', views.Paris, name='Paris'),
    path('pasdedeux/', views.pasdedeux, name='pasdedeux'),
    path('result/', views.result, name='result'),
    path('result2/', views.result2, name='result2'),
    path('romeo/', views.romeo, name='romeo'),
    path('talisman/', views.talisman, name='talisman'),
    path('variation/', views.variation, name='variation'),
    path('featuring/', views.featuring, name='featuring'),
    path('indexa/', views.indexa, name='indexa'),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3')

]