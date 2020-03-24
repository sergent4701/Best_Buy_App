from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login(request):
    return render(request, 'LoginSystem/login.html')


def signup(request):
    return render(request, 'LoginSystem/signup.html')

