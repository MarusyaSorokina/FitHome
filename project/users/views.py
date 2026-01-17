from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from programs.models import FavouriteExercise
from .forms import UserLoginForm, UserRegistrationForm, ProfileUpdateForm
from django.contrib import auth, messages



def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                messages.success(request, 'Вы успешно авторизированны!')
                return redirect('coach')
    else:
        form = UserLoginForm()
    context = {'title': "Авторизация",
               'form': form
               }
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            subject = 'Поздравляем! Ваш аккаунт создан.'
            message = username + "! Добро пожаловать в FitHome! Вы успешно зарегистрировались!"
            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL.HOST.USER,
                    [email]
                )
            except BadHeaderError:
                return HttpResponse('Обнаружен неверный заголовок!')
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('login')
    else:
        form = UserRegistrationForm()


    context = {
        'title': "Регистрация",
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлён!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)  # ← Заполняем форму текущими данными

    favourites = FavouriteExercise.objects.filter(user=request.user).select_related('exercise')
    return render(request, 'users/profile.html', {
        'form': form,
        'favourites': favourites
    })

    # Получаем избранные упражнения текущего пользователя
    favourites = FavouriteExercise.objects.filter(user=request.user).select_related('exercise')  # Оптимизация: загружаем упражнение сразу

    context = {
        'favourites': favourites,
        # Другие данные профиля (например, request.user.username)
    }
    return render(request, 'users/profile.html', context)


    return render(request, 'users/profile.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Вы вышли из учетной записи')
    return redirect('index')

