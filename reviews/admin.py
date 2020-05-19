from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['title', 'description', 'book__title',
                     'book__author__first_name', 'book__author__last_name']
    list_display = ['title', 'book', 'user', 'state', 'pub_date']
    list_filter = ['state', 'book', 'book__author']


admin.site.register(Review, ReviewAdmin)
