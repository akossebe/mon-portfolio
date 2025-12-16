from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
