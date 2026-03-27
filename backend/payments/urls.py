from django.urls import path
from .views import *

urlpatterns = [
    path('create/', PaymentCreateView.as_view()),
    path('list/', PaymentListView.as_view()),
    path('pay/<int:pk>/', PaymentPayView.as_view()),
    path('<int:pk>/', PaymentDetailView.as_view()),
    path('update/<int:pk>/', PaymentUpdateView.as_view()),
    path('delete/<int:pk>/', PaymentDeleteView.as_view()),
    path('pay/<int:pk>/', mark_payment_paid),
]