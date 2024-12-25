from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_view, name='portfolio_view'),
    path('edit/', views.edit_portfolio, name='edit_portfolio'),
]
