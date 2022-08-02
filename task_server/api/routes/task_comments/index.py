from django.urls import path
from task_server.api.views.task_comment.index import createTaskComment, getTaskComments, updateTaskComment, \
                                                     updateTaskState

urlpatterns = [
    path('create', createTaskComment, name='create-task'),
    path('<int:pk>', getTaskComments, name='get-task'),
    path('update', updateTaskComment, name='update-task'),
    path('state', updateTaskState, name='update-state'),
]