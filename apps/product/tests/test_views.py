from django.test import TestCase, Client

from django.contrib.auth.models import User
from django.urls import reverse


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
        self.product_list_url = reverse('product:product-list')
        self.product_add_url = reverse('product:product-add')

    def test_product_list_get(self):
        response = self.client.get(self.product_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product-list.html')

    def test_single_product_post(self):
        product = {
            ''
        }
        response = self.client.post(self.product_add_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product-list.html')
