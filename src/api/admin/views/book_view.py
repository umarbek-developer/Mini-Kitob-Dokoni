from rest_framework.viewsets import ModelViewSet

from apps.kitob.models import Book
from api.admin.serializers.book_serializer import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

