from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login(request):
    return render(request, 'LoginSystem/LoginSystem.html')


def SignUp(request):
    return render(request, 'LoginSystem/SignUp.html')

