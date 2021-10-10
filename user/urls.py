from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.CreateUserAPIView.as_view()),
]
