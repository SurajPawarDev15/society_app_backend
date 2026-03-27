from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import generics, permissions
from django.utils.timezone import now
from .models import Notice
from .serializers import NoticeSerializer

# from core.permissions import IsAdmin
# class NoticeCreateView(generics.CreateAPIView):
#     permission_classes = [IsAdmin]

# 🔹 Create Notice (Admin only)
class NoticeCreateView(generics.CreateAPIView):
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != 'admin':
            raise PermissionDenied("Only admin can create notices")

        serializer.save(created_by=self.request.user)


# 🔹 List Notices (All users)
class NoticeListView(generics.ListAPIView):
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Notice.objects.all().order_by('-created_at')

        # Optional: filter expired notices
        return queryset.filter(expiry_date__gte=now().date()) | queryset.filter(expiry_date__isnull=True)


# CREATE
class NoticeCreateView(generics.CreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# READ ALL
class NoticeListView(generics.ListAPIView):
    queryset = Notice.objects.all().order_by('-created_at')
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]

# READ SINGLE
class NoticeDetailView(generics.RetrieveAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]

# UPDATE
class NoticeUpdateView(generics.UpdateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]

# DELETE
class NoticeDeleteView(generics.DestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]