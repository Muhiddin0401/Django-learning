from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def funk4(request):
    return HttpResponse("Bu 4-funksiya")
def funk5(request):
    return HttpResponse("Bu 5-funksiya")
def funk6(request):
    return HttpResponse("Bu 6-funksiya")

