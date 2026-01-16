from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Programs, Exercise


def program(request, category_id=None):
    context = {
        'title': "FitHome - Тренировки",
        'categories': Programs.objects.all(),

    }
    if category_id:
        exercise = Exercise.objects.filter(category_id=category_id)

    else:
        exercise = Exercise.objects.all()


    paginator = Paginator(exercise, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context.update({'exercise': page_obj})

    return render(request, 'programs/program.html', context)


def workouts(request, pk):
    program_obj = Exercise.objects.get(id=pk)
    context = {
        'title': program_obj.name,
        'exercise': program_obj,
        'categories': Programs.objects.all(),
    }

    return render(request, 'programs/workouts.html', context)



