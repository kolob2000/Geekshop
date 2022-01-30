from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from adminapp.forms import ShopUserAdminChangeForm, CategoryEditForm
from authapp.models import ShopUser
from authapp.forms import ShopUserCreationForm
from mainapp.models import Category


@user_passes_test(lambda user: user.is_superuser)
def main(request):
    context = {
        'title': 'Администрирование',
        'users': ShopUser.objects.all()
    }
    return render(request, 'adminapp/index.html', context=context)


@user_passes_test(lambda user: user.is_superuser)
def user_create(request):
    if request.method == 'POST':
        form = ShopUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin:index')
    else:
        form = ShopUserCreationForm
    context = {
        'title': 'Создать пользователя',
        'form': form,
    }
    return render(request, 'adminapp/user_create.html', context=context)


@user_passes_test(lambda user: user.is_superuser)
def user_update(request, pk):
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        form = ShopUserAdminChangeForm(request.POST, request.FILES, instance=edit_user)
        if form.is_valid():
            form.save()
            return redirect('admin:index')
    else:
        form = ShopUserAdminChangeForm(instance=edit_user)
    context = {
        'title': 'Изменить данные',
        'form': form,
    }
    return render(request, 'adminapp/user_edit.html', context=context)


@user_passes_test(lambda user: user.is_superuser)
def user_delete(request, pk):
    user = ShopUser.objects.get(pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return render(request, 'adminapp/includes/ajax-users.html', context={'users': ShopUser.objects.all(), })


@user_passes_test(lambda user: user.is_superuser)
def category_read(request):
    context = {
        'categories': Category.objects.all(),
        'title': 'Категории',
    }
    return render(request, 'adminapp/categories.html', context=context)


@user_passes_test(lambda user: user.is_superuser)
def category_update(request, pk=None):
    if pk:
        edit_category = get_object_or_404(Category, pk=pk)
        if request.method == 'POST':
            form = CategoryEditForm(request.POST, instance=edit_category)
            if form.is_valid():
                form.save()
                return redirect('admin:category_read')
        else:
            form = CategoryEditForm(instance=edit_category)
    else:
        if request.method == 'POST':
            new_category = CategoryEditForm(request.POST)
            if new_category.is_valid():
                new_category.save()
                return redirect('admin:category_read')
        else:
            form = CategoryEditForm()
    context = {
        'title': 'Редактировать категорию',
        'form': form,
    }
    return render(request, 'adminapp/category_edit.html', context=context)


@user_passes_test(lambda user: user.is_superuser)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if category.is_active:
        category.is_active = False
    else:
        category.is_active = True
    category.save()
    return render(request, 'adminapp/includes/ajax-category.html', context={'categories': Category.objects.all(), })
