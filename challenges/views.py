from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
# from django.template.loader import render_to_string
from django.urls import reverse


monthly_challenges = {
    "january": "Eat only meat for the entire month",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Play with your kids for at least 1 hour every day.",
    "may": None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge(request, month: str):
    try:
        response_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": response_text,
            "month": month
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()


def monthly_challenge_by_number(request, month: int):
    if month > len(monthly_challenges) or month < 1:
        return HttpResponseNotFound("This month is not supported!")

    months = list(monthly_challenges.keys())
    redirect_month: str = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
