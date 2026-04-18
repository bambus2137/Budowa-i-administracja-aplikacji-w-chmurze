from .models import Task
from .serializers import TaskSerializer
from .serializers import TaskValidateSerializer
from django.db import connection
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def api_root(request):
    return Response({
        "tasks": "/api/tasks/",
        "admin": "/admin/",
    })

@api_view(['GET'])
def api_dashboard(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")

        return Response({
            "status": "ok",
            "message": "API is running",
            "database": "connected",
            "endpoints": {
                "tasks": "/api/tasks/",
                "validate": "/api/dashboard/validate/"
            }
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "status": "error",
            "message": "Database or server issue",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def validate_task(request):
    serializer = TaskValidateSerializer(data=request.data)

    if serializer.is_valid():
        return Response({
            "status": "valid",
            "data": serializer.validated_data
        }, status=status.HTTP_200_OK)

    return Response({
        "status": "invalid",
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
