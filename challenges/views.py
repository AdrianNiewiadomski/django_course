from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


monthly_challenges = {
    "january": "Eat only meat for the entire month",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Play with your kids for at least 1 hour every day."
}


def monthly_challenge(request, month: str):
    if month not in monthly_challenges:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(monthly_challenges[month])


def monthly_challenge_by_number(request, month: int):
    if month > len(monthly_challenges) or month < 1:
        return HttpResponseNotFound("This month is not supported!")

    month: str = list(monthly_challenges.keys())[month - 1]
    return HttpResponse(monthly_challenges[month])
