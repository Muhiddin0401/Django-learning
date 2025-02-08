from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def func1(request):
    return HttpResponse("M")

def func2(request):
    return HttpResponse("MU")

def func3(request):
    return HttpResponse("MUH")