from django.contrib.auth.models import User, UserManager
from django import forms
from authapp.models import PizzaShop


class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class PizzaShopForm(forms.ModelForm):
    # береться клас forms.ModelForm тому, що в нас вже є модель PizzaShop
    class Meta:
        model = PizzaShop
        fields = ('name', 'logo')
