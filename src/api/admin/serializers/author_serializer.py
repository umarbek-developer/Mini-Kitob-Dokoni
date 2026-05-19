from rest_framework.serializers import ModelSerializer
from apps.kitob.models import Author


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'