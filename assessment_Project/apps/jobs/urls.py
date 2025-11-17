# apps/jobs/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, ApplyView, MyApplicationsView, ApplicantsForJobView

router = DefaultRouter()
router.register(r"jobs", JobViewSet, basename="job")

urlpatterns = [
    path("", include(router.urls)),
    path("apply/", ApplyView.as_view(), name="apply"),
    path("myapplications/", MyApplicationsView.as_view(), name="myapplications"),
    path("jobs/<int:job_id>/applicants/", ApplicantsForJobView.as_view(), name="job_applicants"),
]
