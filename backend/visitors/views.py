from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from django.utils.timezone import now
from .models import Visitor
from .serializers import VisitorSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Visitor

# 🔹 Create Visitor (Resident)
class VisitorCreateView(generics.CreateAPIView):
    serializer_class = VisitorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(resident=self.request.user)


# 🔹 List Visitors
class VisitorListView(generics.ListAPIView):
    serializer_class = VisitorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Admin देखेगा सब
        if user.role == 'admin':
            return Visitor.objects.all().order_by('-id')

        # Resident अपने visitors
        if user.role == 'resident':
            return Visitor.objects.filter(resident=user)

        # Security सब visitors देखेगा
        if user.role == 'security':
            return Visitor.objects.all()


# 🔹 Approve / Reject (Resident)
class VisitorApproveView(generics.UpdateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = [permissions.IsAuthenticated]


# 🔹 Entry (Security)
class VisitorEntryView(generics.UpdateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(status='entered', entry_time=now())


# 🔹 Exit (Security)
class VisitorExitView(generics.UpdateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(status='exited', exit_time=now())


@api_view(['PUT'])
def approve_visitor(request, pk):
    try:
        visitor = Visitor.objects.get(id=pk)
        visitor.status = 'approved'
        visitor.save()
        return Response({"message": "Visitor Approved"})
    except Visitor.DoesNotExist:
        return Response({"error": "Visitor not found"}, status=404)

@api_view(['PUT'])
def visitor_entry(request, pk):
    try:
        visitor = Visitor.objects.get(id=pk)

        visitor.status = 'entered'
        visitor.entry_time = now()
        visitor.save()

        return Response({
            "message": "Visitor entered successfully",
            "entry_time": visitor.entry_time
        })

    except Visitor.DoesNotExist:
        return Response({"error": "Visitor not found"}, status=404)


@api_view(['PUT'])
def visitor_exit(request, pk):
    try:
        visitor = Visitor.objects.get(id=pk)

        visitor.status = 'exited'
        visitor.exit_time = now()
        visitor.save()

        return Response({
            "message": "Visitor exited successfully",
            "exit_time": visitor.exit_time
        })

    except Visitor.DoesNotExist:
        return Response({"error": "Visitor not found"}, status=404)