from django.urls import path

from info import views

app_name = "info"
urlpatterns = [
    path('', views.home, name='home'),
    path('writing', views.writing_overview, name='writing'),
]
