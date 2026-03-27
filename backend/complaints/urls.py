from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ComplaintCreateView.as_view()),
    path('list/', ComplaintListView.as_view()),
    path('<int:pk>/', ComplaintDetailView.as_view()),
    path('update/<int:pk>/', ComplaintUpdateView.as_view()),
    path('delete/<int:pk>/', ComplaintDeleteView.as_view()),
]