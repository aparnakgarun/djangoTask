from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_showcase, name='project_showcase'),
    #path('add/', views.add_project, name='add_project'),
]
