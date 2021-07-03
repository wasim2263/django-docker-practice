from django.test import TestCase, Client

from django.contrib.auth.models import User
from django.urls import reverse

from apps.product.models import Category, Product


class TestProductViews(TestCase):
    def setUp(self) -> None:
        """
               This method runs before the execution of each test case.
               """
        self.client = Client()
        user = User.objects.create_user(
            username='abdullah', is_active=1)
        user.set_password('wasim2263')
        user.save()
        self.client.login(username='abdullah', password='wasim2263')

    def test_product_list_get(self):
        product_list_url = reverse('product:product-list')
        response = self.client.get(product_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product-list.html')

    def test_single_product_post_get(self):
        product_add_url = reverse('product:product-add', kwargs={'product_id': None})
        category = Category.objects.create(name='test-category')
        product = {
            'code': 'test-code',
            'name': 'test-name',
            'unit_price': 50,
            'unit_type': 'kg',
            'stock': 100,
            'category': category.id
        }
        response = self.client.post(product_add_url, product)
        self.assertEquals(response.status_code, 302)

        product_single = Product.objects.filter(code='test-code').first()
        product_single_url = reverse('product:product-edit', kwargs={'product_id': product_single.id})
        response = self.client.get(product_single_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product-add.html')
        product['unit_price'] = 30
        response = self.client.post(product_single_url, product)
        self.assertEquals(response.status_code, 302)
        product_single = Product.objects.filter(code='test-code').first()
        self.assertEquals(product_single.unit_price, 30)
