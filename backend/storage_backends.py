from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class MediaStorage(S3Boto3Storage):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    file_overwrite = False

    def get_object_parameters(self, name):

        s3_object_params = {"ACL": "public-read"}

        return {**s3_object_params, **self.object_parameters.copy()}
