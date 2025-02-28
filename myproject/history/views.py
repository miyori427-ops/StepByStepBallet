from django.shortcuts import render

# Create your views here.
def c17(request):
    return render(request, "history17.html")

def c19(request):
    return render(request, "history19c.html")

def cmodern(request):
    return render(request, "historymodern.html")

def historyindex(request):
    return render(request, "index2.html")


def c14(request):
    return render(request, "index3.html") 

def c16(request):
    return render(request, "index4.html") 

