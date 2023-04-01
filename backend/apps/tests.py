from django.test import TestCase
from django.urls import reverse
from .models import CustomUser, Article, Category
from rest_framework.test import APIClient

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.category = Category.objects.create(
            name='TestCategory'
        )

        self.article = Article.objects.create(
            title='Test Article',
            content='This is a test article.',
            author=self.user,
            category=self.category
        )

    def test_get_articles(self):
        response = self.client.get(reverse('article-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_article(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'New Test Article',
            'content': 'This is a new test article.',
            'category': self.category.id,
            'author': self.user.id
        }
        response = self.client.post(reverse('article-list-create'), data)
        self.assertEqual(response.status_code, 201)


