from django.test import TestCase
from django.urls import reverse
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


class ProductIndexViewTests(TestCase):
    def test_no_questions_created_on_the_index_page(self):
        response = self.client.get(reverse('product:index'))
        self.assertQuerysetEqual(response.context['products'], [])

    def test_product_created_shows_on_list(self):
        """
        test the product list view page when no product
        is created

        """
        product = Product(name='some product',
                          description='some product description', link='http://someurl.com')
        product.save()
        response = self.client.get(reverse('product:index'))
        self.assertQuerysetEqual(
            response.context['products'],
            ['<Product: some product>']
        )


class ProductDetailViewTests(TestCase):
    def test_product_page_404_for_invalid_product(self):
        """
        test the product detail view page displays 404
        for invalid products

        """
        url = reverse('product:detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_product_detail_page_displays_for_valid_product(self):
        """
        test the product detail view page displays product
        for valid product

        """
        product = Product(name='some product',
                          description='some product description',
                          link='http://someurl.com')
        product.save()
        url = reverse('product:detail', args=(product.id,))
        response = self.client.get(url)
        self.assertContains(response, product.name)

