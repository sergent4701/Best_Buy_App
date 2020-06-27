from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Login')
    else:
        form = SignUpForm()
    return render(request, "LoginSystem/signup.html", {"form": form})


def redirect_login(request):
    return redirect("login/")
