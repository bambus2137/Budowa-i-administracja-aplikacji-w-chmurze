from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Models.task import Task
from DTOs.task_read_serializer import TaskReadDto
from DTOs.task_write_serializer import TaskWriteDto

@api_view(['GET'])
def get_task(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(
            {"error": "Task not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = TaskReadDto(task)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_task(request):
    serializer = TaskWriteDto(data=request.data)

    if serializer.is_valid():
        task = serializer.save()

        response_serializer = TaskReadDto(task)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_task(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(
            {"error": "Task not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = TaskWriteDto(task, data=request.data)

    if serializer.is_valid():
        updated_task = serializer.save()

        response_serializer = TaskReadDto(updated_task)

        return Response(
            response_serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(
            {"error": "Task not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
