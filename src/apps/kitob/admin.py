from django.contrib import admin
from .models import Category, Author, Book
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
