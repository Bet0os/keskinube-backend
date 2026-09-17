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

    def validate_category(self, category):
        if category is None:
            return category

        request = self.context.get('request')

        if request and category.business != request.user.business:
            raise serializers.ValidationError(
                'La categoría no pertenece a tu negocio.'
            )

        return category

    def validate_tags(self, tags):
        request = self.context.get('request')

        if request:
            for tag in tags:
                if tag.business != request.user.business:
                    raise serializers.ValidationError(
                        'Una o más etiquetas no pertenecen a tu negocio.'
                    )

        return tags

    def validate_product_type(self, value):
        if value != 'simple':
            raise serializers.ValidationError(
                'Actualmente solo se admite el tipo de producto simple.'
            )

        return value

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])

        product = Product.objects.create(**validated_data)

        for tag in tags:
            ProductTag.objects.create(
                product=product,
                tag=tag
            )

        return product

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if tags is not None:
            instance.tags.set(tags)

        return instance