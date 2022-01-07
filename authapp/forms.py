import re

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import ShopUser


class ShopUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super(ShopUserAuthenticationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autofocus'] = False


class ShopUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            field.widget.attrs['autofocus'] = False

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.match(r'^\d', username):
            raise forms.ValidationError('Имя не должно начинаться с цифры!')
        return username

    def clean_age(self):
        data = self.cleaned_data['age']
        if 18 > data:
            raise forms.ValidationError('Вы слишком молоды!')
        return data

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password1', 'password2')


class ShopUserChangeForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('first_name', 'last_name', 'email', 'age', 'avatar',)

    def __init__(self, *args, **kwargs):
        super(ShopUserChangeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autofocus'] = False
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']

        if data < 18:
            raise forms.ValidationError('Вы слишком молоды!')
        return data
