# books/views.py
from django.views.generic import ListView
from .models import Book


class BookListView(ListView): #new in chap 3 - library
    model = Book
    template_name = "book_list.html"