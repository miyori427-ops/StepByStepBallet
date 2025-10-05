from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, "center/welcome.html")
def center(request):
    return render(request, "center/center.html")

def plie(request):
    return render(request, "center/plie.html")

def tendu(request):
    return render(request, "center/tendu.html")

def jete(request):
    return render(request, "center/jete.html")

def rondjete(request):
    return render(request, "center/rondjete.html")

def rondt(request):
    return render(request, "center/rondt.html")

def fondu(request):
    return render(request, "center/fondu.html")

def frappe(request):
    return render(request, "center/frappe.html")

def rondenl(request):
    return render(request, "center/rondenl.html")

def petitbatt(request):
    return render(request, "center/petitbatt.html")

def fricflac(request):
    return render(request, "center/fricflac.html")

def developpe(request):
    return render(request, "center/developpe.html")

def panche(request):
    return render(request, "center/panche.html")

def grandbatman(request):
    return render(request, "center/grandbatman.html")

def balancoire(request):
    return render(request, "center/balancoire.html")
    



