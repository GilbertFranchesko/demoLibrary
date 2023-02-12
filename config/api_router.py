from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from demolibrary.book.api.views import AuthorViewSet, BookTypeViewSet, BookViewSet
from demolibrary.users.api.views import UserFavoriteBooksViewSet, UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("user/favorite_books", UserFavoriteBooksViewSet, basename="Book")
router.register("books", BookViewSet)
router.register("books/authors", AuthorViewSet)
router.register("books/types", BookTypeViewSet)

app_name = "api"
urlpatterns = router.urls
