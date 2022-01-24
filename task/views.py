from django.shortcuts import render
from .models import Users
from .forms import UsersForm
from django.contrib import messages


def index(request):
    form = UsersForm(request.POST)
    username = ''
    if form.is_valid():
        username = form.cleaned_data.get("name")
        try:
            Users.objects.get(name=username)
            messages.add_message(request, messages.INFO,
                                 f"Вже бачилися, {username}")
        except Users.DoesNotExist:
            form.save()
            messages.add_message(request, messages.INFO, f"Привіт {username}!")
    form = UsersForm()
    return render(request, '/Users/nikita/projects/task/templates/index.html', {'form': form})


def users(request):
    users = Users.objects.all()
    return render(request, 'templates/users_list.html', {'users': users})