from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('data-description', views.data_description, name='data-description'),
    path('data-visualization', views.data_visualzation, name='data-visualization'),
    path('predictive-models', views.prediction_model, name='predictive-models'),
    path('download-dataset', views.downloader, name='download-dataset'),
]