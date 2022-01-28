from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


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
        response_text += f"<li><a href=\"{redirect_path}\">{month.capitalize()}</a></li>"
    response_text += "</ul>"

    return HttpResponse(response_text)


def monthly_challenge(request, month: str):
    try:
        # response_text = monthly_challenges[month]
        response_text = render_to_string("challenges/challenge.html")
        return HttpResponse(response_text)
    except:    
        return HttpResponseNotFound("This month is not supported!")
    


def monthly_challenge_by_number(request, month: int):
    if month > len(monthly_challenges) or month < 1:
        return HttpResponseNotFound("This month is not supported!")

    months = list(monthly_challenges.keys())
    redirect_month: str = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
