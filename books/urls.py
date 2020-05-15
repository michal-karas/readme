from django.urls import include, path
from django.conf.urls import url

from . import views


app_name = 'books'
urlpatterns = [
    path('authors/', views.AuthorList.as_view(), name='list-authors'),
    path('authors/<int:pk>', views.AuthorDetailsView.as_view(), name='author-details'),
    path('categories/', views.CategoryList.as_view(), name='list-categories'),
    path('books/', views.BookList.as_view(), name='list-books'),
    path('books/<int:pk>', views.BookDetailsView.as_view(), name='book-details'),
    path('categories/<int:pk>', views.CategoryDetailsView.as_view(), name='category-details'),
    path('comments/', include('django_comments.urls')),
    ]
