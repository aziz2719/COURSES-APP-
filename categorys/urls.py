from django.urls import path
from .views import CategoryView, CategoryDetail

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
]