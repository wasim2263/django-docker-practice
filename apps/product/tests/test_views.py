from django.test import TestCase, Client, RequestFactory

from django.contrib.auth.models import User
from django.urls import reverse


class TestProductViews(TestCase):
    def setUp(self) -> None:
        """
               This method runs before the execution of each test case.
               """
        self.client = Client()
        self.factory = RequestFactory()
        user = User.objects.create_user(
            username='abdullah', is_active=1)
        user.set_password('wasim2263')
        user.save()
        self.client.login(username='abdullah', password='wasim2263')


    def test_product_list_get(self):
        response = self.client.get(reverse('product:product-list'))

        # req = RequestFactory().get('/')
        # req.user = AnonymousUser()
        # resp = views.ExampleView.as_view()(req, *[], **{})

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product-list.html')
