from django.urls import reverse
from django.test import TestCase

from books.models import Book

class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse('books:list'))

        self.assertContains(response, 'No books found')
    def test_books_list(self):
        Book.objects.create(title='Book 1', description='Description 1', isbn='1234341')
        Book.objects.create(title='Book 2', description='Description 2', isbn='4141232')
        Book.objects.create(title='Book 3', description='Description 3', isbn='53254')

        response = self.client.get(reverse('books:list'))

        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)

    def test_detail_page(self):
        book = Book.objects.create(title='Book 1', description='Description 1', isbn='1234341')

        response = self.client.get(reverse('books:detail', kwargs={"pk": book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)
