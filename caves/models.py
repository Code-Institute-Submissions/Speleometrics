from django.db import models
from django.contrib.auth.models import User


# Create your models here.

RELEV_SURVEYED = ((0, "Yes"), (1, "No"))


RELEVANCE = (
    (0, "Maximum"), 
    (1, "High"), 
    (2, "Medium"), 
    (3, "Low")
)


GEOMORPH_UNIT = (
    (0, "Serra da Serpentina"),
    (2, "Itabira"),
    (3, "Serra da Piedade"),
    (4, "João Monlevade"),
    (5, "Quadrilátero Oeste"),
    (6, "Serra Azul"),
    (7, "Morrarias de Dom Bosco"),
    (8, "Serra de Ouro Preto - Antonio Pereira"),
    (9, "Escarpa Oriental do Caraça"),
    (10, "Serra do Gandarela"),
)


class Cave(models.Model):
    cave_name = models.CharField(max_length=40, unique=True, blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    elevation = models.IntegerField(blank=False)
    length = models.FloatField(blank=False)
    depth = models.FloatField(blank=False)
    area = models.FloatField(blank=False)
    volume = models.FloatField(blank=False)
    relevance_surveyed = models.IntegerField(choices=RELEV_SURVEYED, default=0)
    relevance_factor = models.IntegerField(choices=RELEVANCE, default=0)
    geomorph_unit = models.IntegerField(choices=GEOMORPH_UNIT, default=0, blank=False)
    description = models.TextField(blank=True)  # Optional description field
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name="cave_reg"
    )

    class Meta:
        ordering = ["cave_name"]
    
    def __str__(self):
        return f"{self.cave_name} registered by {self.author}"