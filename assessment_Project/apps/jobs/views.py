# apps/jobs/views.py
from rest_framework import viewsets, generics, mixins, status
from rest_framework.response import Response
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from .permissions import IsEmployer, IsEmployerOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by("-created_at")
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsEmployerOrReadOnly]

    def get_permissions(self):
        # Allow list & retrieve for authenticated users; create/update/delete restricted by IsEmployerOrReadOnly object permission
        if self.action in ["list","retrieve"]:
            return [IsAuthenticated()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get("q")
        location = self.request.query_params.get("location")
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
        if location:
            qs = qs.filter(location__icontains=location)
        return qs

class ApplyView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Only applicants can apply
        if request.user.role != "applicant":
            return Response({"detail":"Only applicants can apply."}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

class MyApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user).order_by("-applied_at")

class ApplicantsForJobView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsEmployer]

    def get_queryset(self):
        job_id = self.kwargs.get("job_id")
        qs = Application.objects.filter(job_id=job_id).order_by("-applied_at")
        # Ensure current user is owner of the job
        if not qs.exists():
            return Application.objects.none()
        # extra check: job posted_by == request.user
        from .models import Job
        try:
            job = Job.objects.get(pk=job_id)
            if job.posted_by != self.request.user:
                return Application.objects.none()
        except Job.DoesNotExist:
            return Application.objects.none()
        return qs
