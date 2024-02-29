from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
      model = Project
      fields = ('id','title','decription','tecnologia','created_at')
      read_only_fields = ('created_at',)
  