from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class UserFavoriteBooksViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer

    def create(self, *args, **kwargs):
        favorite_books = self.request.data.get("favorite_books", None)

        self.request.user.favorite_books.add(favorite_books)
        self.request.user.save()

        serializer = UserSerializer(
            self.request.user, context={"request": self.request}
        )
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
