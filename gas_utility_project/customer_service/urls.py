from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add a URL pattern for your app
]
