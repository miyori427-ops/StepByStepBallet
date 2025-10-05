from django.urls import path
from . import views
app_name = 'center'
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('center', views.center, name='center'), 
    path('plie/', views.plie, name='plie'),
    path('tendu/', views.tendu, name='tendu'),
    path('jete/', views.jete, name='jete'),
    path('rondjete/', views.rondjete, name='rondjete'),
    path('rondt/', views.rondt, name='rondt'),
    path('fondu/', views.fondu, name='fondu'),
    path('frappe/', views.frappe, name='frappe'),
    path('rondenl/', views.rondenl, name='rondenl'),
    path('petitbatt/', views.petitbatt, name='petitbatt'),
    path('fricflac/', views.fricflac, name='fricflac'),
    path('developpe/', views.developpe, name='developpe'),
    path('panche/', views.panche, name='panche'),
    path('grandbatman/', views.grandbatman, name='grandbatman'),
    path('balancoire/', views.balancoire, name='balancoire'),] 