from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import newEntryForm
from .models import Entry
from django.http import Http404


# Create your views here.
def dashboard(request):
    return render(request, "main/dashboard.html")


def newEntry(request):
    if not request.user.is_authenticated:
        raise Http404

    if request.method == "POST":
        form = newEntryForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            entry = form.save(commit=False)
            entry.employee = request.user
            entry.dateCreated = timezone.now()
            entry.save()
            #return redirect('Dashboard')
    else:
        form = newEntryForm()
    return render(request, 'main/newEntry.html', {'form': form})


def listUsers(request):
    users = User.objects.all()
    return render(request, 'main/userList.html', {'users': users})


def displayEntries(request, pk):
    user = get_object_or_404(User, pk=pk)
    entries = Entry.objects.filter(employee=user)
    return render(request, 'main/entryList.html', {'user': user, 'entries': entries})


def displayEntry(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = newEntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save()
            entry.save()
            return redirect('Dashboard')
    else:
        form = newEntryForm(instance=entry)
    return render(request, 'main/entry.html', {'form': form})
