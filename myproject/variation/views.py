from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def aurora(request):
    return render(request, "aurora.html")

def blackswan(request):
    return render(request, "blackswan.html")

def Cinderella(request):
    return render(request, "Cinderella.html")

def gayane(request):
    return render(request, "gayane.html")

def Kaizoku(request):
    return render(request, "Kaizoku.html")

def Paris(request):
    return render(request, "Paris.html") 

def pasdedeux(request):
    return render(request, "pasdedeux.html") 

def result(request):
    return render(request, "result.html")

def result2(request):
    return render(request, "result2.html")

def romeo(request):
    return render(request, "romeo.html") 

def talisman(request):
    return render(request, "talisman.html") 


@csrf_protect
def variation(request):
    if request.method == 'POST':
        selected_option = request.POST.get('option')
        if selected_option == 'はい':
            return redirect('result')
        elif selected_option == 'いいえ':
            return redirect('result2')
        else:
            return redirect('featuring')
    return render(request, 'variation.html')


def featuring(request):
    return render(request, "featuring.html")  

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

def index2(request):
    return render(request, "index2.html")  

def index3(request):
    return render(request, "index3.html")  

