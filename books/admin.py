from django.contrib import admin
from .models import Category, Book

admin.site.register(Category)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    list_filter = ('author', 'title', 'category')
    search_fields = ('author','title')