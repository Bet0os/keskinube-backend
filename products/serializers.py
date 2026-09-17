from rest_framework import serializers
from .models import Category, Tag, Product, ProductTag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'sku',
            'sale_price',
            'cost',
            'stock',
            'product_type',
            'is_visible',
            'category',
            'tags',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])

        product = Product.objects.create(**validated_data)

        for tag in tags:
            ProductTag.objects.create(
                product=product,
                tag=tag
            )

        return product