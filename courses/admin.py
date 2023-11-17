from django.contrib import admin
from .models import Course, Profession

admin.site.register((Course, Profession))