from django.urls import path
from auth.views import register

urlpatterns = [
    path('register/', register, name='register'),
]
