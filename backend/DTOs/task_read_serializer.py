from rest_framework import serializers
from Models.task import Task


class TaskReadDto(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed']

