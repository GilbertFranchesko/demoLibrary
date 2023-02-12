from book.models import Author, Book, BookType
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import GenericViewSet

from .serializers import AuthorSerializer, BookSerializer, BookTypeSerializer


class BookViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]

        elif self.request.method == "PATCH":
            self.permission_classes = [
                AllowAny,
            ]

        elif self.request.method == "POST":
            self.permission_classes = [
                IsAdminUser,
            ]

        elif self.request.method == "DELETE":
            self.permission_classes = [
                IsAdminUser,
            ]

        return super().get_permissions()


class BookTypeViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = BookTypeSerializer
    queryset = BookType.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]

        elif self.request.method == "PATCH":
            self.permission_classes = [
                AllowAny,
            ]

        elif self.request.method == "POST":
            self.permission_classes = [
                IsAdminUser,
            ]

        elif self.request.method == "DELETE":
            self.permission_classes = [
                IsAdminUser,
            ]

        return super().get_permissions()


class AuthorViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [
                AllowAny,
            ]

        elif self.request.method == "PATCH":
            self.permission_classes = [
                AllowAny,
            ]

        elif self.request.method == "POST":
            self.permission_classes = [
                IsAdminUser,
            ]

        elif self.request.method == "DELETE":
            self.permission_classes = [
                IsAdminUser,
            ]

        return super().get_permissions()
