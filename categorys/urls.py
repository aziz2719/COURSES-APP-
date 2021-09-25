from django.urls import path
from .views import *

urlpatterns = [
    path('course/', CourseView.as_view()),
    path('course/<int:pk>/', CourseDetailView.as_view()),
]
