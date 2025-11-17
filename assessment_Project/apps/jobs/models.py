# apps/jobs/models.py
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="jobs")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.location}"

class Application(models.Model):
    STATUS_CHOICES = (
        ("applied","Applied"),
        ("shortlisted","Shortlisted"),
        ("rejected","Rejected"),
        ("accepted","Accepted"),
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applications")
    resume_link = models.URLField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="applied")
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("job","applicant")
