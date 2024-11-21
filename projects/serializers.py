from rest_framework import serializers
from .models import Project
from taggit.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True
    )
    technologies = TagListSerializerField()

    class Meta:
        model = Project
        fields = ('id', 'title', 'image', 'description', 'technologies', 'created_at')
        read_only_fields = ("created_at",)