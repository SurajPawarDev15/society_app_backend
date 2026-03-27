from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Complaint
from .serializers import ComplaintSerializer

# 🔹 Create Complaint
class ComplaintCreateView(generics.CreateAPIView):
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 🔹 List Complaints
# class ComplaintListView(generics.ListAPIView):
#     serializer_class = ComplaintSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user

#         # Admin देखेगा सभी complaints
#         if user.role == 'admin':
#             return Complaint.objects.all()

#         # Resident सिर्फ अपने complaints देखेगा
#         return Complaint.objects.filter(user=user)
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class ComplaintListView(generics.ListAPIView):
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]

    queryset = Complaint.objects.all().order_by('-created_at')

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'category', 'priority']
    search_fields = ['title', 'description']

    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return self.queryset

        return self.queryset.filter(user=user)

# 🔹 Update Status (Admin only)
class ComplaintUpdateView(generics.UpdateAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]

def detect_category_priority(text):
    text = text.lower()

    if "water" in text:
        return "water", "high"
    elif "electric" in text:
        return "electricity", "high"
    elif "security" in text:
        return "security", "medium"

    return "other", "low"

def perform_create(self, serializer):
    description = self.request.data.get('description', '')
    
    category, priority = detect_category_priority(description)

    serializer.save(
        user=self.request.user,
        category=category,
        priority=priority
    )

    # ✅ DELETE
class ComplaintDeleteView(generics.DestroyAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]

# ✅ RETRIEVE (Single Complaint)
class ComplaintDetailView(generics.RetrieveAPIView):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]