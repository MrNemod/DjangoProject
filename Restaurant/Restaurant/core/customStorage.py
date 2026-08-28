from django.conf import settings
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from imagekitio import ImageKit
import os

@deconstructible
class imageKitStorage(Storage):
    def __init__(self):
        self.client = ImageKit(
            private_key=settings.IMAGEKIT_PRIVATE_KEY
        )

    def _save(self, name, content):
        #Leer imagen
        file_bytes = content.read()
        file_name = os.path.basename(name)
        folder = os.path.dirname(name.replace('\\', '/'))

        #Subir la imagen
        upload_response = self.client.files.upload(
            file=file_bytes,
            file_name=file_name,
            folder = f"/{folder}" if folder else "/",
            use_unique_file_name = True
        )
        #Obtener ruta del archivo subido
        if hasattr(upload_response, 'file_path') and upload_response.file_path:
            return upload_response.file_path.lstrip('/')

        # Fallback de seguridad si ImageKit devuelve solo el nombre
        return getattr(upload_response, 'name', file_name)

    def exists(self, name):
        return False

    def url(self, name):
        base_endpoint = settings.IMAGEKIT_URL_ENDPOINT.rstrip('/')
        return f'{base_endpoint}/{name.lstrip("/")}'