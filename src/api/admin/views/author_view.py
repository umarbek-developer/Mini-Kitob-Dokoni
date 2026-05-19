from rest_framework.viewsets import ModelViewSet

from apps.kitob.models import Author
from api.admin.serializers.author_serializer import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

