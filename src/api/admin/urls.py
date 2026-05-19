from django.urls import path, include
from api.admin.views import category_view, author_view, book_view
from rest_framework.routers import DefaultRouter

r = DefaultRouter()

r.register("category", category_view.CategoryViewSet, basename="categoryviews")
r.register("author", author_view.AuthorViewSet, basename="authorviews")
r.register("book", book_view.BookViewSet, basename="bookviews")


urlpatterns = [
    path('', include(r.urls)),
]