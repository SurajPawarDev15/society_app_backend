from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework import generics, permissions
from django.utils.timezone import now
from .models import Payment
from .serializers import PaymentSerializer


# 🔹 Admin creates maintenance bill
class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# 🔹 List Payments
class PaymentListView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Admin sees all
        if user.role == 'admin':
            return Payment.objects.all()

        # Resident sees own payments
        return Payment.objects.filter(user=user)


# 🔹 Mark as Paid (Resident)
class PaymentPayView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(status='paid', paid_at=now())

# READ SINGLE
class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

# UPDATE (Mark as Paid)
class PaymentUpdateView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

# DELETE
class PaymentDeleteView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]    
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['PUT'])
def mark_payment_paid(request, pk):
    try:
        payment = Payment.objects.get(id=pk)
        payment.status = 'paid'
        payment.payment_date = now()
        payment.save()

        return Response({"message": "Payment Successful"})
    except Payment.DoesNotExist:
        return Response({"error": "Not found"}, status=404)        