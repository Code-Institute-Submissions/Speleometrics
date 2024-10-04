from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
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
    (8, "Serra de Ouro Preto - Antônio Pereira"),
    (9, "Escarpa Oriental do Caraça"),
    (10, "Serra do Gandarela"),
)


class Cave(models.Model):
    """
    Main model establishes the cave data base and its atributes as the field listed bellow 
    """
    cave_name = models.CharField(
        max_length=40,
        unique=True,
        blank=False,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9\s_-]+$',
                message="""Cave name can only contain letters,
                 numbers, spaces, hyphens, and underscores."""
            )
        ],
        help_text="""Enter a unique name. Letters, numbers,
         spaces, hyphens, and underscores are allowed."""
    )

    lat_long_validator = RegexValidator(
        regex=r'^(?![+-]00\.000000$)[+-]\d{2}\.\d{6}$',
    )

    latitude = models.FloatField(
        blank=False,
        validators=[lat_long_validator],
        help_text="""Please enter the latitude coordinate
         in the Decimal Degrees format (e.g., -20.102852)"""
    )

    longitude = models.FloatField(
        blank=False,
        validators=[lat_long_validator],
        help_text="""Please enter the longitude coordinate
         in the Decimal Degrees format (e.g., -43.453612)"""
    )

    elevation = models.IntegerField(
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(3000)
        ],
        help_text="""Enter values between 0 and 3000 with
         no significant decimal digits."""
    )

    length = models.FloatField(
        blank=False,
        validators=[
            MinValueValidator(5),
            MaxValueValidator(3000)
        ],
        help_text="""Enter values between 5 and 3000 with significant
         decimal digits separated by a period (e.g., 12.34)."""
    )

    depth = models.FloatField(
        blank=False,
        validators=[
            MinValueValidator(0.10),
            MaxValueValidator(500)
        ],
        help_text="""Enter valid values (>0 - 500) with significant
         decimal digits separated by a period (e.g., 123.45)."""
    )

    area = models.FloatField(
        blank=False,
        validators=[
            MinValueValidator(0.10),
            MaxValueValidator(3000)
        ],
        help_text="""Enter valid values (>0 - 3000) with significant
         decimal digits separated by a period (e.g., 123.45)."""
    )

    volume = models.FloatField(
        blank=False,
        validators=[
            MinValueValidator(0.10),
            MaxValueValidator(3000)
        ],
        help_text="""Enter valid values (>0 - 3000) with significant
         decimal digits separated by a period (e.g., 123.45)."""
    )
    
    lithology = models.CharField(max_length=40, blank=False)

    relevance_surveyed = models.IntegerField(choices=RELEV_SURVEYED, default=0)

    relevance_factor = models.IntegerField(choices=RELEVANCE, default=0)

    geomorph_unit = models.IntegerField(
        choices=GEOMORPH_UNIT,
         default=0,
          blank=False
    )

    description = models.TextField(blank=True)

    cave_maps = CloudinaryField("cave_maps",
        resource_type="auto",
        folder="caves_maps",
        blank=True,
        help_text="JPG or PDF are supported formats."
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_cave", null=True, blank=True
    )

    
    class Meta:
        """
        Orders caves alphabetically by their name atribute
        """
        ordering = ["cave_name"]

    def __str__(self):
        return f"{self.cave_name} registered by {self.user}"
