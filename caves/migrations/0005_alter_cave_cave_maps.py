# Generated by Django 4.2.16 on 2024-10-05 19:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caves', '0004_alter_cave_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cave',
            name='cave_maps',
            field=cloudinary.models.CloudinaryField(blank=True, help_text='Only JPG or PNG formats are supported.', max_length=255, verbose_name='cave_maps'),
        ),
    ]
