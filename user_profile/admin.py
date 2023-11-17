from django.contrib import admin
from user_profile.models import Profile, UserCourse

admin.site.register((Profile, UserCourse))