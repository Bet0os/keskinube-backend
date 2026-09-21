from django.db import models
from businesses.models import Business


class Category(models.Model):
    name = models.CharField(max_length=100)
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name='categories'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'business'],
                name='unique_category_name_per_business'
            )
        ]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name='tags'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'business'],
                name='unique_tag_name_per_business'
            )
        ]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500, blank=True)
    sku = models.CharField(max_length=100, blank=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    stock = models.PositiveIntegerField()

    product_type = models.CharField(
        max_length=50,
        default='simple'
    )

    is_visible = models.BooleanField(default=True)

    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name='products'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )

    tags = models.ManyToManyField(
        Tag,
        through='ProductTag',
        related_name='products',
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductTag(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE
    )