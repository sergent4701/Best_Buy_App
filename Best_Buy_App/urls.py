"""Best_Buy_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from LoginSystem import views as loginViews
from main import views as mainViews
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', loginViews.signup, name="Sign Up"),
    path('', loginViews.redirect_login, name="Login"),
    path('login/', LoginView.as_view(), name="Login"),
    path("logout/", LogoutView.as_view(), name="Logout"),

    path('dashboard/', mainViews.dashboard, name="Dashboard"),
    path('entry/new/', mainViews.newEntry, name='New Entry'),
    path('entry/<int:pk>/', mainViews.displayEntry, name='Entry'),
    path('user_list/', mainViews.listUsers, name='User List'),
    path('userEntryList/<int:pk>/', mainViews.displayEntries, name='User Entry List'),
]
