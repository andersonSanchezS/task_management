from django.urls import path
from task_server.api.views.incidence_comment.index import createIncidenceComment, getIncidenceComments, \
                                                          updateIncidenceComment, updateIncidenceState


urlpatterns = [
    path('create', createIncidenceComment, name='create-task'),
    path('<int:pk>', getIncidenceComments, name='get-task'),
    path('update', updateIncidenceComment, name='update-task'),
    path('state', updateIncidenceState, name='update-state'),
]
