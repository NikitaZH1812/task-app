from django.forms import ModelForm, TextInput
from .models import Users


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name']
        widgets = {'name': TextInput
                   (attrs={'placeholder': 'Введи своє ім\'я'})}