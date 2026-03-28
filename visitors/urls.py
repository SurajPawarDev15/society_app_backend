from django.urls import path
from .views import *

urlpatterns = [
    path('create/', VisitorCreateView.as_view()),
    path('list/', VisitorListView.as_view()),
    path('approve/<int:pk>/', VisitorApproveView.as_view()),
    path('approve/<int:pk>/', approve_visitor),
    path('entry/<int:pk>/', VisitorEntryView.as_view()),
    path('entry/<int:pk>/', visitor_entry),
    path('exit/<int:pk>/', VisitorExitView.as_view()),
    path('exit/<int:pk>/', visitor_exit),
    path('<int:pk>/', generics.RetrieveAPIView.as_view(
    queryset=Visitor.objects.all(),
    serializer_class=VisitorSerializer
)),
]