from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
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

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'FitHome - Профиль',
               'form': form
               }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    messages.success(request, 'Вы вышли из учетной записи')
    return redirect('index')