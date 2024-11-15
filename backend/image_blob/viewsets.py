from rest_framework import viewsets
from .serializers import ImageBlobSerializer
from .models import ImageBlob
from django_filters.rest_framework import DjangoFilterBackend


class ImageBlobViewSet(viewsets.ModelViewSet):
    queryset = ImageBlob.objects.all()
    serializer_class = ImageBlobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "uuid",
    ]


class ImageBlobUUIDViewSet(viewsets.ModelViewSet):
    queryset = ImageBlob.objects.all()
    serializer_class = ImageBlobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "uuid",
    ]
    lookup_field = "uuid"
