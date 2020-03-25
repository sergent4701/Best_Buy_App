from django.contrib import admin
from .models import Entries, Users, Goals

admin.site.register(Users)
admin.site.register(Entries)
admin.site.register(Goals)

