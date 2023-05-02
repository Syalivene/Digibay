import os
from django.db import models
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io


# Create your models here.


STATUS = (
    (0, "Brand new"),
    (1, "Used"),
    (2, "Other"),
)

STOCK = (
    (0, "Single"),
    (1, "Medium"),
    (2, "Large"),
    (3, "Extra-large"),
    (4, "Unlimited")
)


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    price2 = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='item_image', blank=True, null='True', default='default_images/default_image_item.jpg')
    image2 = models.ImageField(upload_to='item_image2', blank=True, null='True', default='default_images/default_image2_item.jpg')
    image3 = models.ImageField(upload_to='item_image3', blank=True, null='True', default='default_images/default_image3_item.jpg')
    is_sold = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    stock = models.IntegerField(choices=STOCK, default=0)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']

    #def __str__(self):
    #    return self.name
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            if img.format != 'JPEG':
                buffer = io.BytesIO()
                img.convert('RGB').save(buffer, format='JPEG', quality=60)
                buffer.seek(0)
                self.image = SimpleUploadedFile(self.image.name, buffer.read(), content_type='image/jpeg')
                img = Image.open(self.image)

            img.thumbnail((600, 600))
            buffer = io.BytesIO()
            img.save(buffer, format='JPEG', quality=60)
            buffer.seek(0)
            self.image = SimpleUploadedFile(self.image.name, buffer.read(), content_type='image/jpeg')

        if self.image2:
            img = Image.open(self.image2)
            if img.format != 'JPEG':
                buffer = io.BytesIO()
                img.convert('RGB').save(buffer, format='JPEG', quality=60)
                buffer.seek(0)
                self.image2 = SimpleUploadedFile(self.image2.name, buffer.read(), content_type='image/jpeg')
                img = Image.open(self.image2)

            img.thumbnail((300, 300))
            buffer = io.BytesIO()
            img.save(buffer, format='JPEG', quality=60)
            buffer.seek(0)
            self.image2 = SimpleUploadedFile(self.image2.name, buffer.read(), content_type='image/jpeg')

        if self.image3:
            img = Image.open(self.image3)
            if img.format != 'JPEG':
                buffer = io.BytesIO()
                img.convert('RGB').save(buffer, format='JPEG', quality=60)
                buffer.seek(0)
                self.image3 = SimpleUploadedFile(self.image3.name, buffer.read(), content_type='image/jpeg')
                img = Image.open(self.image3)

            img.thumbnail((300, 300))
            buffer = io.BytesIO()
            img.save(buffer, format='JPEG', quality=60)
            buffer.seek(0)
            self.image3 = SimpleUploadedFile(self.image3.name, buffer.read(), content_type='image/jpeg')

        super(Item, self).save(*args, **kwargs)




    def delete(self, *args, **kwargs):
        # Delete the images from storage
        if self.image and hasattr(self.image, 'path'):
            os.remove(self.image.path)
        if self.image2 and hasattr(self.image2, 'path'):
            os.remove(self.image2.path)
        if self.image3 and hasattr(self.image3, 'path'):
            os.remove(self.image3.path)

        # Call the default delete() method to delete the object from the database
        super().delete(*args, **kwargs)
