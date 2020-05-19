from django.shortcuts import reverse
from django.contrib.auth.mixins import AccessMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin

from django.db.models import Avg, Count

from reviews.forms import GradeForm
from .models import Author, Book, Category


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Strona główna',
    }

    # def get_context_data(self, **kwargs):
    #     context = {
    #         'best_books': Book.objects.filter().order_by()
    #     }
    #     context.update(kwargs)
    #     return super().get_context_data(**context)


class AuthorList(ListView):
    model = Author
    template_name = 'books/list_authors.html'
    extra_context = {
        'title': 'Wszyscy autorzy',
    }


class AuthorDetail(DetailView):
    model = Author
    template_name = 'books/author_details.html'

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Author {self.object}',
        }
        context.update(kwargs)
        return super().get_context_data(**context)


class BookList(ListView):
    model = Book
    template_name = 'books/list_books.html'
    extra_context = {
        'title': 'Wszyskie książki',
    }


# from django.contrib.auth.mixins import AccessMixin
class BookDetail(AccessMixin, SingleObjectMixin, FormView):
    model = Book
    template_name = 'books/book_details.html'
    form_class = GradeForm

    def get_success_url(self):
        return reverse('books:book-details', kwargs={'pk': self.object.pk})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.object
        self.grade = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Book {self.object.title} by {self.object.author}',
            # SELECT AVG('grade') as average, COUNT('grade') as count
            # FROM grades WHERE book_id=???
            'avg_grades': self.object.grade_set.aggregate(
                average=Avg('grade'), count=Count('grade')
            ),
        }
        context.update(kwargs)
        return super().get_context_data(**context)


class CategoryList(ListView):
    model = Category
    template_name = 'books/list_categories.html'
    extra_context = {
        'title': 'Wszystkie kategorie',
    }


class CategoryDetail(DetailView):
    model = Category
    template_name = 'books/category_details.html'

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Category {self.object}',
        }
        context.update(kwargs)
        return super().get_context_data(**context)
