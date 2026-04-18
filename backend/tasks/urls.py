from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDeleteView
from .views import api_dashboard, validate_task

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view()),
    path('dashboard/', api_dashboard),
    path('dashboard/validate/', validate_task),
]
