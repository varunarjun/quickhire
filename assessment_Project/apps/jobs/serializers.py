# apps/jobs/serializers.py
from rest_framework import serializers
from .models import Job, Application
from apps.users.serializers import UserSerializer

class JobSerializer(serializers.ModelSerializer):
    posted_by = UserSerializer(read_only=True)
    class Meta:
        model = Job
        fields = ("id","title","description","salary","location","posted_by","created_at")

class ApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)
    job_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Application
        fields = ("id","job","job_id","applicant","resume_link","status","applied_at")
        read_only_fields = ("status","applied_at")

    def create(self, validated_data):
        job_id = validated_data.pop("job_id")
        request = self.context["request"]
        from .models import Job
        job = Job.objects.get(pk=job_id)
        application = Application.objects.create(job=job, applicant=request.user, **validated_data)
        return application
