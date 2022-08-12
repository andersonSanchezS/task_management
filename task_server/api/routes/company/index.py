from django.urls import path
from task_server.api.views.company.index import getCompany, createCompany, updateCompany, deleteCompany, getCompanyTeam

urlpatterns = [
    path('get/<int:pk>', getCompany, name='get-company'),
    path('create', createCompany, name='create-company'),
    path('update/<int:pk>', updateCompany, name='update-company'),
    path('delete/<int:pk>', deleteCompany, name='delete-company'),
    path('workers', getCompanyTeam, name='get-company-team'),
]