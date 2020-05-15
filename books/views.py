from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Book, Category


class AuthorList(ListView):
    model = Author
    template_name = 'books/list_authors.html'
    extra_context = {
        'title': 'Wszyscy autorzy',
    }


class AuthorDetailsView(DetailView):
    template_name = 'books/authors_details.html'
    model = Author


class BookList(ListView):
    model = Book
    template_name = 'books/list_books.html'
    extra_context = {
        'title': 'Wszyskie książki',
    }


class BookDetailsView(DetailView):
    model = Book
    template_name = 'books/book_details.html'
    context_object_name = "book"
    extra_context = {
        'title': 'Books',
    }


class CategoryList(ListView):
    model = Category
    template_name = 'books/list_categories.html'
    extra_context = {
        'title': 'Wszystkie kategorie',
    }


class CategoryDetailsView(DetailView):
    model = Category
    template_name = 'books/category_details.html'
    context_object_name = "category"
    extra_context = {
        'title': 'Category',
    }
