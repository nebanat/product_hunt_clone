from django.test import TestCase
from .models import Product
from .forms import ProductForm


# Create your tests here.
class ProductModelTests(TestCase):
    def test_product_was_successfully_created(self):
        """
        new product was successfully created
        """
        new_product = Product(name='a new product',
                              description='some description', link='http://someproduct.com')
        self.assertIs(new_product.name, 'a new product')


class ProductFormTests(TestCase):
    def test_blank_data(self):
        form = ProductForm({})
        self.assertFalse(form.is_valid())

    def test_valid_data(self):
        form = ProductForm({
            'name': 'Some products',
            'description': 'some product description',
            'link': 'http://somelink.com'
        })

        self.assertTrue(form.is_valid())
        new_product = form.save()
        self.assertEqual(new_product.name, 'Some products')
        self.assertEqual(new_product.description, 'some product description')
        self.assertEqual(new_product.link, 'http://somelink.com')
