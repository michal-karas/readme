from django.urls import path

from . import views


app_name = 'books'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('authors/', views.AuthorList.as_view(), name='list-authors'),
    path('authors/<int:pk>', views.AuthorDetail.as_view(), name='author-details'),
    path('books/', views.BookList.as_view(), name='list-books'),
    path('books/<int:pk>', views.BookDetail.as_view(), name='book-details'),
    path('categories/', views.CategoryList.as_view(), name='list-categories'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name='category-details'),
]
