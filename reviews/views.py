from django.contrib.auth.mixins import LoginRequiredMixin
from certifi.__main__ import args
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import View
from django.views.generic.list import ListView
from .model import Review
from .books.models import Book


class AddReview(CreateView):
    model = Review
    template_name = 'reviews/add.html'
    fields = ['title', 'content', 'grade']

    def get_book(self):
        book_id = self.kwargs.get('book_id')
        return get_object_or_404(Book, pk=book_id)

    def get(self, request, *arg, **kwargs):
        self.book = self.get_book()
        return super().post(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        self.book = self.get_book()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.book
        form.instance.state = 'draft'
        return super().form_valid(form)


class EditReview(UpdateView):
    model = Review
    pk_url_kwarg = 'review_id'
    template_name = 'reviews/edit.html'
    fields = ['title', 'content', 'grade']

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user, state='draft')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.object.book
        form.instance.state = 'draft'
        return super().form_valid(form)


class PublishReview(View):
    def post(self, request, *args, **kwargs):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id)
        review.state = 'in_moderation'
        review.save()
        return redirect('reviews:list-reviews')


class ListReviews(ListView):
    template_name = 'reviews/list.html'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user, state='draft')
