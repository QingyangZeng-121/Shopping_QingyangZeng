from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product,ProductBrand


class ProductTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product_brand=ProductBrand.objects.create(
            name='Test product_brand',
        )
        self.product = Product.objects.create(
            title='Test Product',
            describe='This is a test product',
            product_brand=self.product_brand,
            price=10.00,
            inventory=100
        )

    def test_product_detail_view(self):
        response = self.client.get(reverse('detail'), {"id":self.product.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.title)

    def test_purchase_view(self):
        response = self.client.get(reverse('purchase'), {'id': self.product.id, 'product_count': 1})
        self.assertEqual(response.status_code, 200)

    def test_cancellation_view(self):
        response = self.client.get(reverse('cancellation'), {'id': 1})
        self.assertEqual(response.status_code, 200)

    def test_statistics_view(self):
        response = self.client.get(reverse('statistics'))
        self.assertEqual(response.status_code, 200)


    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_area_view(self):
        response = self.client.get(reverse('area'))
        self.assertEqual(response.status_code, 200)
