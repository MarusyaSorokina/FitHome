from django.shortcuts import render
from .models import Coach, Photo, CoachCategory


def index(request):
    return render(request, 'coach/index.html', {'title': 'FitHome'})


def coach(request):
    tren = Coach.objects.all()
    context = {
        'title': 'FitHome - тренировки',
        'categories': CoachCategory.objects.all(),
        "coach": tren,
    }
    return render(request, "coach/coach.html", context)



