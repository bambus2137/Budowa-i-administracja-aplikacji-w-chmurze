from rest_framework import serializers
from Models.task import Task

class TaskSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=200)

    class Meta:
        model = Task
        fields = '__all__'
