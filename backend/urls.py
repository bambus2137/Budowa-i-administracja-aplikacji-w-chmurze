from django.urls import path
from Controllers import tasks_controller

urlpatterns = [
    path('tasks/', tasks_controller.get_tasks),
    path('tasks/<int:id>/', tasks_controller.get_task),
    path('tasks/create/', tasks_controller.create_task),
    path('tasks/update/<int:id>/', tasks_controller.update_task),
    path('tasks/delete/<int:id>/', tasks_controller.delete_task),
]
