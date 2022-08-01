from django.urls import path
from task_server.api.views.task.index import createTask, getTasks, updateTask, updateTaskState

urlpatterns = [
    path('create', createTask, name='create-task'),
    path('list/<int:pk>', getTasks, name='get-tasks'),
    path('update/<int:pk>', updateTask, name='update-task'),
    path('state/<int:pk>', updateTaskState, name='update-task-state'),
]