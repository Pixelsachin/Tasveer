from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import os

# from django.core.validators import validate_image_file_extension


# Create your models here.


def filename(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".jpg"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("only jpg file can be uploded")


class img_load(models.Model):
    image = models.ImageField(upload_to="images/", validators=[filename])
    uploaded_at = models.DateTimeField(default=timezone.now)
