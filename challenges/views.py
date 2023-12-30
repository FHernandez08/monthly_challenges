from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk at least 20 minutes every day!",
    "march": "Learning django the most this month.",
    "april": "My birthday is in this month",
    "may": "My mom's birthday is in this month.",
    "june": "Still summer time",
    "july": "Summer Time!",
    "august": "The start of the school semester",
    "september": "I think fall starts this month",
    "october": "Have a happy halloween",
    "november": "Happy Thanksgiving!",
    "december": None
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month.")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
