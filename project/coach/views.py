from django.shortcuts import render
from .models import Coach, Photo


def index(request):
    return render(request, 'coach/index.html', {'title': 'FitHome'})


def coach(request):
    tren = Coach.objects.all()
    context = {
        "coach": tren,
    }
    return render(request, "coach/coach.html", context)

def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'coach/gallery.html', {'photos': photos})

