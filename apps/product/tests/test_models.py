from django.test import TestCase

from apps.product.models import Product


class TestProductModel(TestCase):
    def setUp(self) -> None:
        product = Product.objects.create()