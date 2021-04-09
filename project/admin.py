from django.contrib import admin
from .models import Project
from .models import Client
# Register your models here.
admin.site.register(Project)
admin.site.register(Client)