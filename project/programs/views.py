from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Programs, Exercise, FavouriteExercise


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
    if not request.user.is_authenticated:
        return redirect('register')
    program_obj = get_object_or_404(Exercise, id=pk)
    context = {
        'title': program_obj.name,
        'exercise': program_obj,
        'categories': Programs.objects.all(),
    }
    return render(request, 'programs/workouts.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация успешна! Теперь войдите в аккаунт.")
            return redirect('login')
        else:
            messages.error(request, "Проверьте ошибки в форме.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'programs/register.html', {'form': form})


@login_required
def add_to_favourites(request, exercise_id):
    try:
        exercise = get_object_or_404(Exercise, id=exercise_id)
        fav, created = FavouriteExercise.objects.get_or_create(
            user=request.user,
            exercise=exercise
        )
        if created:
            messages.success(request, "Упражнение добавлено в избранное!")
        else:
            messages.info(request, "Уже в избранном")
    except Exception as e:
        messages.error(request, f"Ошибка: {e}")


    return redirect('profile')  # ← Редирект на профиль из users


@login_required
def remove_from_favourites(request, exercise_id):
    try:
        exercise = get_object_or_404(Exercise, id=exercise_id)
        FavouriteExercise.objects.filter(
            user=request.user,
            exercise=exercise
        ).delete()
        messages.success(request, "Упражнение удалено из избранного!")
    except Exception as e:
        messages.error(request, f"Ошибка: {e}")


    return redirect('profile')  # Возвращаемся на страницу профиля