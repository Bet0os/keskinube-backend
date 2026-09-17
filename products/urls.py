from django.urls import path

from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    TagListCreateView,
    TagDetailView,
    ProductListCreateView,
    ProductDetailView,
)

urlpatterns = [
    path(
        'categories/',
        CategoryListCreateView.as_view(),
        name='category-list-create'
    ),
    path(
        'categories/<int:pk>/',
        CategoryDetailView.as_view(),
        name='category-detail'
    ),

    path(
        'tags/',
        TagListCreateView.as_view(),
        name='tag-list-create'
    ),
    path(
        'tags/<int:pk>/',
        TagDetailView.as_view(),
        name='tag-detail'
    ),

    path(
        '',
        ProductListCreateView.as_view(),
        name='product-list-create'
    ),
    path(
        '<int:pk>/',
        ProductDetailView.as_view(),
        name='product-detail'
    ),
]