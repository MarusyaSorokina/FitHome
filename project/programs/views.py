from django.shortcuts import render, redirect
from .models import Programs, Exercise


def program(request, category_id=None):
    context = {
        'title': "FitHome - Тренировки",
        'categories': Programs.objects.all()
    }
    if category_id:
        context.update({
            'exercise': Exercise.objects.filter(category_id=category_id)
        })
    else:
        context.update({
            'exercise': Exercise.objects.all()
        })

    return render(request, 'programs/program.html', context)


def workouts(request, pk):
    program_obj = Exercise.objects.get(id=pk)
    context = {
        'title': program_obj.name,
        'exercise': program_obj,
        'categories': Programs.objects.all(),
    }

    return render(request, 'programs/workouts.html', context)



