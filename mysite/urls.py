from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('projects/', views.projects, name="projects"),
    path('contact/', views.contact, name="contact")
]
