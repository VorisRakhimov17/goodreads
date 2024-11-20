from idlelib.textview import ViewWindow

from django.shortcuts import render
from django.views import View

from books.models import Book

class BooksView(View):
    def get(self, request):
        books = Book.objects.all()

        return render(request, "books/list.html", {"books": books})

class BookDetailView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, "books/detail.html", {"book": book})

