from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def ackount(request):
    return render(request, 'main/ackount.html')