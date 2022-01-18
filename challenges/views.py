from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(reqest):
    return HttpResponse("Eat only meat for the entire month")


def february(request):
    return HttpResponse("Walk for at least 20 minutes every day")


def monthly_challenge(request, month):
    return HttpResponse(f"Challenge for {month}")
