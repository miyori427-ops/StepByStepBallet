from django.shortcuts import render

def acting(request):
    return render(request, "acting.html")  

def featuring(request):
    return render(request, "featuring.html")  



