# Generated by Django 4.2.16 on 2024-10-04 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('caves', '0003_cave_cave_maps_alter_cave_geomorph_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cave',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_cave', to=settings.AUTH_USER_MODEL),
        ),
    ]