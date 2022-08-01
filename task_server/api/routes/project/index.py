from django.urls import path
from task_server.api.views.project.index import getProjects, getProject, createProject,\
                                                updateProject, updateState

urlpatterns = [
    path('list', getProjects, name='get-projects'),
    path('<int:pk>', getProject, name='get-project'),
    path('create', createProject, name='create-project'),
    path('update/<int:pk>', updateProject, name='update-project'),
    path('state/<int:pk>', updateState, name='update-state'),
]