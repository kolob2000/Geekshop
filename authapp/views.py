import django.contrib.auth.backends
from django.contrib import auth, messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse

from geekshop import settings
from .forms import ShopUserAuthenticationForm, ShopUserCreationForm, ShopUserChangeForm, ShopUserProfileForm
from .models import ShopUser, ShopUserProfile


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
            if send_verify_key(user):
                messages.success(request, 'На почту отправленно письмо с подтверждением!')
            else:
                user.delete()
                messages.error(request, 'Ошибка регистрации. Попробуйте снова.')
            return redirect('auth:login')
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
        edit_profile_form = ShopUserProfileForm(request.POST, request, instance=request.user.shopuserprofile)
        if edit_form.is_valid() and edit_profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:user_profile'))
    else:
        edit_form = ShopUserChangeForm(instance=request.user)
        edit_profile_form = ShopUserProfileForm(instance=request.user.shopuserprofile)
    context = {
        'title': 'Редактировать данные пользователя',
        'form': edit_form,
        'edit_form': edit_profile_form
    }
    return render(request, 'authapp/user_edit.html', context=context)


def user_profile(request):
    context = {
        'title': 'Профиль пользователя'
    }
    return render(request, 'authapp/user_profile.html', context=context)


def send_verify_key(request_user: ShopUser):
    subject = 'Подтверждение регистрации'
    link = reverse('auth:verify', args=[request_user.email, request_user.activation_key])
    message = f'Подтвердите регистрацию на сайте {settings.DOMAIN_NAME} перейдя по ссылке:\n' \
              f' {settings.DOMAIN_NAME}:8000{link}'
    mail = send_mail(subject, message, settings.EMAIL_HOST_USER, (request_user.email,), fail_silently=True)
    return mail


def verify(request, email, key):
    user = get_object_or_404(ShopUser, email=email)

    if user.activation_key_expires and user.activation_key == key and user.activation_key != 'registered':
        user.is_active = True
        user.activation_key = 'registered'
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect(reverse('auth:user_edit'))
    else:
        return render(request, 'authapp/confirmation_error.html', context={
            'title': 'Ошибка регистрации'
        })
