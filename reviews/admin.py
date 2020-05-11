from django.contrib import admin
from .models import Review, Grade


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'pub_data', 'state', 'grade',)
    list_filter = ('user', 'title', 'content', 'pub_data', 'state', 'grade',)
    search_fields = ('user', 'title', 'content', 'pub_data', 'state', 'grade',)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('user', 'grade', 'book',)
    list_filter = ('user', 'grade', 'book',)
    search_fields = ('user', 'grade', 'book',)


admin.site.register(Review, ReviewAdmin)
admin.site.register(Grade, GradeAdmin)


# Register your models here.
