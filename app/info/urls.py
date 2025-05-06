from django.urls import path

from django_distill import distill_path
from info import views

app_name = "info"
urlpatterns = [
    distill_path('', views.home, name='home', distill_file='index.html'),
    distill_path('writing', views.writing_overview, name='writing', distill_file='writing.html'),
]
