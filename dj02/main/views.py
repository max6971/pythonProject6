from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return render(request,'main/index.html')
def new (request):
    return render(request,'main/new.html')

def three (request):
    return render(request,'main/three.html')

def onas (request):
    return render(request,'main/onas.html')
