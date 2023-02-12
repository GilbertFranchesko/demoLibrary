from book.api.serializers import BookSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url", "favorite_books"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class FavoriteBooksSerializer(serializers.Serializer):
    favorite_books = BookSerializer(read_only=True, many=True)
