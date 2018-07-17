from django.test import TestCase
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.urls import reverse
from product.models import Product
from .models import Comment
from .forms import CommentForm


def test_data_sync():
    User.objects.create_user(username='anothertestuser',
                             email='anothertestuser@gmail.com',
                             password='sometestpassword')

    Product.objects.create(name='hello product',
                           description='hello description',
                           link='http://hellolink.com',
                           user=User.objects.get(username='anothertestuser'))


# Create your tests here.
class CommentModelTests(TestCase):
    def setUp(self):
        test_data_sync()

    def test_comment_was_successfully_created(self):

        user = User.objects.get(username='anothertestuser')
        product = Product.objects.get(name='hello product')
        comment = Comment(text='hello product comment', user=user,
                          product=product)
        self.assertIs(comment.user.username, user.username)

    def test_raise_key_error_exception_with_no_product(self):
        with self.assertRaises(IntegrityError):
            comment = Comment(text='another comment')
            comment.save()


class CommentViewTest(TestCase):
    def setUp(self):
        test_data_sync()

    def test_get_method_not_allowed_on_comment_view(self):
        response = self.client.get(reverse('comment:new'))
        self.assertEqual(response.status_code, 405)

    def test_that_comment_displays_on_product_page(self):
        user = User.objects.get(username='anothertestuser')
        product = Product.objects.get(name='hello product')
        comment = Comment.objects.create(text='hello product comment',
                                         user=user,
                                         product=product)
        response = self.client.get(reverse('product:detail', args=(product.id,)))
        self.assertContains(response, comment.text)
        self.assertContains(response, comment.user.username)

    def test_that_no_comment_shows_for_product_with_no_comment(self):
        product = Product.objects.get(name='hello product')
        response = self.client.get(reverse('product:detail', args=(product.id,)))
        self.assertContains(response, 'No comments on this product yet!')


class CommentFormTest(TestCase):
    def setUp(self):
        test_data_sync()

    def test_comment_form_invalid_with_no_data(self):
        form = CommentForm({})
        self.assertFalse(form.is_valid())

    def test_comment_form_valid_with_saved_data(self):
        form = CommentForm({
            'text': 'some random comment'
        })
        self.assertTrue(form.is_valid())
        user = User.objects.get(username='anothertestuser')
        product = Product.objects.get(name='hello product')
        form.instance.user = user
        form.instance.product = product
        comment = form.save()
        self.assertEqual(comment.text, 'some random comment')
        self.assertEqual(comment.user.username, user.username)
        self.assertEqual(comment.product.name, product.name)

    def test_form_throws_integrity_error_for_no_product_or_user(self):
        form = CommentForm({
            'text': 'some random comment'
        })
        with self.assertRaises(IntegrityError):
            form.save()



