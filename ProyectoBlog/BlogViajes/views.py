from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "principal.html")

def agregar(request):
    pass
