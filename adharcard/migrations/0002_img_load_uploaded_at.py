# Generated by Django 5.1 on 2024-08-28 08:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adharcard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='img_load',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
