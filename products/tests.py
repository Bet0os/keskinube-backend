from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from businesses.models import Business
from .models import Category, Tag, Product


class ProductRelatedTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='alberto@test.com',
            email='alberto@test.com',
            password='Test12345!'
        )

        self.business = Business.objects.create(
            name='Beto Company',
            user=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_create_category(self):
        response = self.client.post(
            '/api/products/categories/',
            {
                'name': 'Tecnología'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        category = Category.objects.get(name='Tecnología')

        self.assertEqual(
            category.business,
            self.business
        )

    def test_create_tag(self):
        response = self.client.post(
            '/api/products/tags/',
            {
                'name': 'Oferta'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        tag = Tag.objects.get(name='Oferta')

        self.assertEqual(
            tag.business,
            self.business
        )

    def test_list_categories(self):
        Category.objects.create(
            name='Electrónica',
            business=self.business
        )

        response = self.client.get(
            '/api/products/categories/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.data),
            1
        )

    def test_list_tags(self):
        Tag.objects.create(
            name='Promoción',
            business=self.business
        )

        response = self.client.get(
            '/api/products/tags/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.data),
            1
        )

    def test_update_category(self):
        category = Category.objects.create(
            name='Electrónica',
            business=self.business
        )

        response = self.client.patch(
            f'/api/products/categories/{category.id}/',
            {
                'name': 'Tecnología'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        category.refresh_from_db()

        self.assertEqual(
            category.name,
            'Tecnología'
        )

    def test_delete_category(self):
        category = Category.objects.create(
            name='Temporal',
            business=self.business
        )

        response = self.client.delete(
            f'/api/products/categories/{category.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Category.objects.filter(
                id=category.id
            ).exists()
        )

    def test_update_tag(self):
        tag = Tag.objects.create(
            name='Oferta',
            business=self.business
        )

        response = self.client.patch(
            f'/api/products/tags/{tag.id}/',
            {
                'name': 'Promoción'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        tag.refresh_from_db()

        self.assertEqual(
            tag.name,
            'Promoción'
        )

    def test_delete_tag(self):
        tag = Tag.objects.create(
            name='Temporal',
            business=self.business
        )

        response = self.client.delete(
            f'/api/products/tags/{tag.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Tag.objects.filter(
                id=tag.id
            ).exists()
        )

    def test_create_product(self):
        category = Category.objects.create(
            name='Tecnología',
            business=self.business
        )

        tag = Tag.objects.create(
            name='Oferta',
            business=self.business
        )

        response = self.client.post(
            '/api/products/',
            {
                'name': 'Laptop HP',
                'description': 'Laptop para uso general',
                'sku': 'LAP-001',
                'sale_price': '1299.00',
                'cost': '950.00',
                'stock': 15,
                'product_type': 'simple',
                'is_visible': True,
                'category': category.id,
                'tags': [tag.id]
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        product = Product.objects.get(
            name='Laptop HP'
        )

        self.assertEqual(
            product.business,
            self.business
        )

        self.assertEqual(
            product.category,
            category
        )

        self.assertEqual(
            product.tags.count(),
            1
        )

    def test_list_products(self):
        Product.objects.create(
            name='Mouse Logitech',
            description='Mouse inalámbrico',
            sku='MOU-001',
            sale_price='45.00',
            cost='25.00',
            stock=50,
            product_type='simple',
            is_visible=True,
            business=self.business
        )

        response = self.client.get(
            '/api/products/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.data),
            1
        )

    def test_product_detail(self):
        product = Product.objects.create(
            name='Teclado',
            description='Teclado mecánico',
            sku='TEC-001',
            sale_price='80.00',
            cost='50.00',
            stock=10,
            product_type='simple',
            is_visible=True,
            business=self.business
        )

        response = self.client.get(
            f'/api/products/{product.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['name'],
            'Teclado'
        )

    def test_update_product(self):
        product = Product.objects.create(
            name='Monitor',
            description='Monitor 24 pulgadas',
            sku='MON-001',
            sale_price='200.00',
            cost='150.00',
            stock=8,
            product_type='simple',
            is_visible=True,
            business=self.business
        )

        response = self.client.patch(
            f'/api/products/{product.id}/',
            {
                'sale_price': '220.00',
                'stock': 12,
                'is_visible': False
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        product.refresh_from_db()

        self.assertEqual(
            str(product.sale_price),
            '220.00'
        )

        self.assertEqual(
            product.stock,
            12
        )

        self.assertFalse(
            product.is_visible
        )

    def test_delete_product(self):
        product = Product.objects.create(
            name='Producto temporal',
            description='Temporal',
            sku='TEMP-001',
            sale_price='10.00',
            cost='5.00',
            stock=1,
            product_type='simple',
            is_visible=True,
            business=self.business
        )

        response = self.client.delete(
            f'/api/products/{product.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Product.objects.filter(
                id=product.id
            ).exists()
        )

    def test_user_cannot_see_products_from_another_business(self):
        other_user = User.objects.create_user(
            username='other@test.com',
            email='other@test.com',
            password='Test12345!'
        )

        other_business = Business.objects.create(
            name='Other Company',
            user=other_user
        )

        Product.objects.create(
            name='Producto privado',
            description='No debe aparecer',
            sku='PRIVATE-001',
            sale_price='100.00',
            cost='50.00',
            stock=5,
            product_type='simple',
            is_visible=True,
            business=other_business
        )

        response = self.client.get(
            '/api/products/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.data),
            0
        )

    def test_user_cannot_access_product_from_another_business(self):
        other_user = User.objects.create_user(
            username='other2@test.com',
            email='other2@test.com',
            password='Test12345!'
        )

        other_business = Business.objects.create(
            name='Other Company 2',
            user=other_user
        )

        product = Product.objects.create(
            name='Producto ajeno',
            description='No debe ser accesible',
            sku='OTHER-001',
            sale_price='100.00',
            cost='50.00',
            stock=5,
            product_type='simple',
            is_visible=True,
            business=other_business
        )

        response = self.client.get(
            f'/api/products/{product.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )