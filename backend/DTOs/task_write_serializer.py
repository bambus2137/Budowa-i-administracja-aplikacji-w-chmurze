from rest_framework import serializers
from Models.task import Task


class TaskWriteDto(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

