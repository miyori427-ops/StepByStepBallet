from django.shortcuts import render

def indexa(request):
    return render(request, 'indexa.html')  # テンプレートを指定