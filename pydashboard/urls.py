from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('data-description', views.data_description, name='data-description'),
    path('descriptive-analysis', views.descriptive_analytics, name='descriptive-analysis'),
    path('data-visualization', views.descriptive_analytics, name='data-visualization'),
    path('predictive-models', views.descriptive_analytics, name='predictive-models'),
    path('download-dataset', views.descriptive_analytics, name='download-dataset'),
]