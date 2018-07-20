from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category
from .forms import ProductForm


def test_sync_data():
    User.objects.create_user(username='johndoe',
                                           password='johnpassword',
                                           email='johndoe@gmail.com')

    Category.objects.create(name='software')
    Category.objects.create(name='apps')



# Create your tests here.
class ProductModelTests(TestCase):
    def setUp(self):
        test_sync_data()

    def test_product_was_successfully_created_with_no_category(self):
        """
        new product was successfully created
        """
        user = User.objects.get(username='johndoe')

        new_product = Product(name='a new product',
                              description='some description',
                              link='http://someproduct.com',
                              user=user)
        self.assertIs(new_product.name, 'a new product')
        self.assertIs(new_product.user.username, user.username)

    def test_product_was_successfully_created_with_category(self):
        user = User.objects.get(username='johndoe')
        category_one = Category.objects.get(name='software')

        new_product = Product(name='a new product',
                              description='some description',
                              link='http://someproduct.com',
                              user=user)
        new_product.save()
        new_product.categories.add(category_one)
        self.assertIs(new_product.name, 'a new product')
        self.assertIs(new_product.user.username, user.username)


class ProductFormTests(TestCase):
    def setUp(self):
        test_sync_data()

    def test_blank_data(self):
        form = ProductForm({})
        self.assertFalse(form.is_valid())

    def test_valid_data_with_one_category(self):
        user = User.objects.get(username='johndoe')
        category=Category.objects.get(name='software')
        form_data = {
            'name': 'Some products',
            'description': 'some product description',
            'link': 'http://somelink.com',

        }
        form = ProductForm(data=form_data)
        form.instance.user = user
        new_product=form.save()
        new_product.categories.add(category)
        self.assertTrue(form.is_valid())
        self.assertEqual(new_product.name, 'Some products')
        self.assertEqual(new_product.description, 'some product description')
        self.assertEqual(new_product.link, 'http://somelink.com')
        self.assertTrue(new_product.categories.exists())
        self.assertEqual(new_product.categories.count(), 1)

    def test_valid_data_with_multiple_data(self):
        user = User.objects.get(username='johndoe')
        category_one = Category.objects.get(name='software')
        category_two = Category.objects.get(name='apps')
        form_data = {
            'name': 'Some products',
            'description': 'some product description',
            'link': 'http://somelink.com',

        }
        form = ProductForm(data=form_data)
        form.instance.user = user
        new_product = form.save()
        new_product.categories.add(category_one, category_two)
        self.assertTrue(new_product.categories.exists())
        self.assertEqual(new_product.categories.count(), 2)


class ProductIndexViewTests(TestCase):
    def setUp(self):
        test_sync_data()

    def test_no_questions_created_on_the_index_page(self):
        response = self.client.get(reverse('product:index'))
        self.assertQuerysetEqual(response.context['products'], [])

    def test_product_created_shows_on_list(self):
        """
        test the product list view page when no product
        is created

        """
        user = User.objects.get(username='johndoe')

        product = Product(name='some product',
                          description='some product description',
                          link='http://someurl.com',
                          user=user)
        product.save()
        response = self.client.get(reverse('product:index'))
        self.assertQuerysetEqual(
            response.context['products'],
            ['<Product: some product>']
        )


class ProductDetailViewTests(TestCase):
    def setUp(self):
        test_sync_data()

    def test_product_page_404_for_invalid_product(self):
        """
        test the product detail view page displays 404
        for invalid products

        """
        url = reverse('product:detail',
                      args=('62081693-df61-4675-a5ac-e9998f575422',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_product_detail_page_displays_for_valid_product(self):
        """
        test the product detail view page displays product
        for valid product

        """
        user = User.objects.get(username='johndoe')

        product = Product(name='some product',
                          description='some product description',
                          link='http://someurl.com',
                          user=user
                          )
        product.save()
        url = reverse('product:detail', args=(product.id,))
        response = self.client.get(url)
        self.assertContains(response, product.name)

