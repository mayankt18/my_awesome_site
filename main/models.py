from django.db import models

class PhotoGallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    upload_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="gallery")