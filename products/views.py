from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Category, Tag, Product
from .serializers import (
    CategorySerializer,
    TagSerializer,
    ProductSerializer,
)


class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(
            business=self.request.user.business
        )

    def perform_create(self, serializer):
        serializer.save(
            business=self.request.user.business
        )


class TagListCreateView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tag.objects.filter(
            business=self.request.user.business
        )

    def perform_create(self, serializer):
        serializer.save(
            business=self.request.user.business
        )


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(
            business=self.request.user.business
        )

    def perform_create(self, serializer):
        serializer.save(
            business=self.request.user.business
        )


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(
            business=self.request.user.business
        )


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(
            business=self.request.user.business
        )


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tag.objects.filter(
            business=self.request.user.business
        )