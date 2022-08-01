from django.urls import path
from task_server.api.views.incidence.index import createIncidence, getIncidences, updateIncidence, \
                                                  updateIncidenceStatus

urlpatterns = [
    path('create', createIncidence, name='create-incidence'),
    path('list/<int:pk>', getIncidences, name='get-incidences'),
    path('update/<int:pk>', updateIncidence, name='update-incidence'),
    path('state/<int:pk>', updateIncidenceStatus, name='update-incidence-state'),
]