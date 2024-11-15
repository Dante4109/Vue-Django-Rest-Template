from rest_framework import routers
from .viewsets import ImageBlobViewSet, ImageBlobUUIDViewSet
from django.urls import path, include

app_name = "image_blob"

# initiate router and register all endpoints
router = routers.DefaultRouter()
router.register(r"image", ImageBlobViewSet, basename="image")
router.register(r"imageUUID", ImageBlobUUIDViewSet, basename="imageUUID")

# Wire up our API with our urls
urlpatterns = [path("", include(router.urls))]
