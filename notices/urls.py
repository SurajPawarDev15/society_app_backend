from django.urls import path
from .views import *

urlpatterns = [
    path('create/', NoticeCreateView.as_view()),
    path('list/', NoticeListView.as_view()),
    path('<int:pk>/', NoticeDetailView.as_view()),
    path('update/<int:pk>/', NoticeUpdateView.as_view()),
    path('delete/<int:pk>/', NoticeDeleteView.as_view()),
]