from django.contrib import admin

from books.models import Author, Category, Book


class BooksInline(admin.StackedInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'web_site')
    list_filter = ('first_name', 'last_name', 'birth_date', 'web_site')
    date_hierarchy = 'birth_date'
    search_fields = ('first_name', 'last_name', 'web_site')
    inlines = [BooksInline]


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages', 'krotki_opis', 'cover')
    list_filter = ('title', 'author', 'categories', 'pages')
    search_fields = ('title', 'description', 'author__first_name', 'author__last_name')

    # Book.objects.filter(author__first_name__startswith='Andrzej')

    def krotki_opis(self, obj):
        return (
            f'{obj.description[:50]}...'
            if len(obj.description) > 50
            else obj.description
        )

    # krotki_opis.short_description = 'Description'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
