from django.urls import path
from task_server.api.views.company.index import getCompany, createCompany

urlpatterns = [
    path('get/<int:pk>', getCompany, name='get-company'),
    path('create', createCompany, name='create-company'),
]