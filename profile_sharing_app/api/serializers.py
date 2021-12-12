from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'