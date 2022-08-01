from django.urls import path
from task_server.api.views.task.index import createTask, getTasks, updateTask, updateTaskState, getTask

urlpatterns = [
    path('create', createTask, name='create-task'),
    path('list/<int:pk>', getTasks, name='get-tasks'),
    path('<int:pk>', getTask, name='get-task'),
    path('update/<int:pk>', updateTask, name='update-task'),
    path('state/<int:pk>', updateTaskState, name='update-task-state'),
]