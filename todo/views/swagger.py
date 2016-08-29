import os

from django.conf import settings
from django.http import FileResponse
from django.views import generic


class Swagger(generic.View):

    def get(self, request):
        swagger_yml_path = os.path.join(
            settings.BASE_DIR,
            '',
            'swagger.yaml',
        )

        swagger_yml = open(swagger_yml_path, 'rb')

        return FileResponse(
            swagger_yml,
            content_type='application/x-yaml',
        )
