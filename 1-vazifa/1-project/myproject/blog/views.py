from django.shortcuts import render

from django.http import HttpResponse

def funk1(request):
    return HttpResponse("Bu 1 - funksiya")
def funk2(request):
    return HttpResponse("Bu 2 - funksiya")
def funk3(reques):
    return HttpResponse("Bu 3 - funksiya")

