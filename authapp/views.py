from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .forms import ShopUserAuthenticationForm, ShopUserCreationForm, ShopUserChangeForm


def login(request):
    if request.method == 'POST':
        login_form = ShopUserAuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('auth:user_profile'))
    else:
        login_form = ShopUserAuthenticationForm()
    context = {
        'title': 'Вход',
        'form': login_form
    }
    return render(request, 'authapp/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    if request.method == 'POST':
        register_form = ShopUserCreationForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('auth:user_profile'))
    else:
        register_form = ShopUserCreationForm()
    context = {
        'title': 'Регистрация',
        'form': register_form
    }
    return render(request, 'authapp/registration.html', context=context)


def user_edit(request):
    if request.method == 'POST':
        edit_form = ShopUserChangeForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:user_profile'))
    else:
        edit_form = ShopUserChangeForm(instance=request.user)
    context = {
        'title': 'Редактировать данные пользователя',
        'form': edit_form
    }
    return render(request, 'authapp/user_edit.html', context=context)


def user_profile(request):
    context = {
        'title': 'Профиль пользователя'
    }
    return render(request, 'authapp/user_profile.html', context=context)
