from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(reqest):
    return HttpResponse("Eat only meat for the entire month")


def february(request):
    return HttpResponse("Walk for at least 20 minutes every day")


def monthly_challenge(request, month: str):
    return HttpResponse(f"Challenge for {month}. month is a {type(month).__name__}")


def monthly_challenge_by_number(request, month: int):
    print(type(month))
    return HttpResponse(f"Challenge for {month}. month is an {type(month).__name__}")
