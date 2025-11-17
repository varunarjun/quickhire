# apps/jobs/admin.py
from django.contrib import admin
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("id","title","location","salary","posted_by","created_at")
    search_fields = ("title","location","description")

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id","job","applicant","status","applied_at")
    list_filter = ("status",)
    search_fields = ("job__title","applicant__username")
