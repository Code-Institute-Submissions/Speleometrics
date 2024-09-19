# Generated by Django 4.2.16 on 2024-09-19 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cave_name', models.CharField(max_length=40, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('elevation', models.IntegerField()),
                ('length', models.FloatField()),
                ('depth', models.FloatField()),
                ('area', models.FloatField()),
                ('volume', models.FloatField()),
                ('relevance_surveyed', models.IntegerField(choices=[(0, 'Yes'), (1, 'No')], default=0)),
                ('relevance_factor', models.IntegerField(choices=[(0, 'Maximum'), (1, 'High'), (2, 'Medium'), (3, 'Low')], default=0)),
                ('geomorph_unit', models.IntegerField(choices=[(0, 'Serra da Serpentina'), (2, 'Itabira'), (3, 'Serra da Piedade'), (4, 'João Monlevade'), (5, 'Quadrilátero Oeste'), (6, 'Serra Azul'), (7, 'Morrarias de Dom Bosco'), (8, 'Serra de Ouro Preto - Antonio Pereira'), (9, 'Escarpa Oriental do Caraça'), (10, 'Serra do Gandarela')], default=0)),
                ('description', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cave_reg', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['cave_name'],
            },
        ),
    ]
