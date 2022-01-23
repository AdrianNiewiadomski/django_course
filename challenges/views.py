from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat only meat for the entire month",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Play with your kids for at least 1 hour every day."
}


def index(request):
    response_text = "<ul>"
    for month in monthly_challenges.keys():
        redirect_path = reverse("month-challenge", args=[month])
        response_text += f"<li><a href=\"{redirect_path}\">{month}</a></li>"
    response_text += "</ul>"

    return HttpResponse(response_text)


def monthly_challenge(request, month: str):
    if month not in monthly_challenges:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(monthly_challenges[month])


def monthly_challenge_by_number(request, month: int):
    if month > len(monthly_challenges) or month < 1:
        return HttpResponseNotFound("This month is not supported!")

    months = list(monthly_challenges.keys())
    redirect_month: str = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
