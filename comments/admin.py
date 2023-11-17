from django.contrib import admin
from comments.models import Comment, Complaint, BlockedComment

admin.site.register((Comment, Complaint, BlockedComment))