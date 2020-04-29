from django.contrib import admin
from .models import Category, Runner, Race

admin.site.register(Runner)
admin.site.register(Category)
admin.site.register(Race)
