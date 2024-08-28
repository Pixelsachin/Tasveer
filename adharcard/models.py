from django.db import models
from django.utils import timezone


# Create your models here.
class img_load(models.Model):
    image = models.ImageField(upload_to="images/")
    uploaded_at = models.DateTimeField(default=timezone.now)
