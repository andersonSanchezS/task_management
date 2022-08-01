from django.urls import path
from task_server.api.views.task_comment.index import createTaskComment, getTaskComments

urlpatterns = [
    path('create', createTaskComment, name='create-task'),
    path('<int:pk>', getTaskComments, name='get-task'),
]