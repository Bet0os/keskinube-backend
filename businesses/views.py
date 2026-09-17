from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Business
from .serializers import BusinessSerializer


class BusinessCreateView(generics.CreateAPIView):
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)