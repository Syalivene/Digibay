from django.db import models
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io
from .choices import ADDRESS




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    second_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(choices=ADDRESS, default="Butembo")
    email = models.EmailField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='app002_profile', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            if img.format != 'JPEG':
                buffer = io.BytesIO()
                img.convert('RGB').save(buffer, format='JPEG', quality=60)
                buffer.seek(0)
                self.image = SimpleUploadedFile(self.image.name, buffer.read(), content_type='image/jpeg')
                img = Image.open(self.image)

            img.thumbnail((200, 200))
            buffer = io.BytesIO()
            img.save(buffer, format='JPEG', quality=60)
            buffer.seek(0)
            self.image = SimpleUploadedFile(self.image.name, buffer.read(), content_type='image/jpeg')

        super(Profile, self).save(*args, **kwargs)

