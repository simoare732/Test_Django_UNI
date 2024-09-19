from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from api.views import BookListAPIView, BookViewSet

app_name = 'api'

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')
urlpatterns = router.urls