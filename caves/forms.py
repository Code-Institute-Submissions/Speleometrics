from django import forms
from django.forms import ModelForm
from .models import Cave

RELEV_SURVEYED = (
    (0, "Yes"),
    (1, "No"),
)

RELEVANCE = (
    (0, "Maximum"),
    (1, "High"),
    (2, "Medium"),
    (3, "Low"),
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


class CaveForm(forms.ModelForm):
    """
    Establishes form for cave registry
    """
    class Meta:
        """
        Add fields, labels, error messages and help messages for CaveForm
        """
        model = Cave
        fields = (
            'cave_name',
            'latitude',
            'longitude',
            'elevation',
            'length',
            'depth',
            'area',
            'volume',
            'lithology',
            'relevance_surveyed',
            'relevance_factor',
            'geomorph_unit',
            'description',
            'cave_maps',
            'user',
        )
        labels = {
            "cave_name": "Cave Name",
            "latitude": "Latitude (Dd)",
            "longitude": "Longitude (Dd)",
            "elevation": "Elevation (m)",
            "length": "Length (m)",
            "depth": "Depth (m)",
            "area": "Area (m²)",
            "volume": "Volume (m³)",
            "lithology": "Lithology",
            "relevance_surveyed": "Was the relevance surveyed?",
            "relevance_factor": "Relevance Factor (if not surveyed = maximum)",
            "geomorph_unit": "Geomorphological Unit",
            "description": "Brief Description",
            "cave_maps": "Cave Maps",
            "user": "User",
        }
        help_texts = {
            "cave_name": """Enter a unique cave name (letters, numbers,
             spaces, hyphens, underscores allowed).""",
            "latitude":
                "Enter latitude in Decimal Degrees format (e.g., -20.102852).",
            "longitude":
                """Enter longitude in Decimal Degrees
                format (e.g., -43.453612).""",
            "elevation": "Enter elevation (0-3000 m).",
            "length": "Enter length (5-3000 m).",
            "depth": "Enter depth (0.10-500 m).",
            "area": "Enter area (0.10-3000 m²).",
            "volume": "Enter volume (0.10-3000 m³).",
            "lithology": "Enter the lithology of the cave.",
            "relevance_surveyed": "Select if the cave has been surveyed.",
            "relevance_factor": "Select the relevance factor.",
            "geomorph_unit": "Select the geomorphological unit.",
            "description": "Provide additional information about the cave.",
            "cave_maps": "JPG or PNG are supported formats.",
        }
        error_messages = {
            "cave_name": {
                'required': "Cave name is required.",
                'unique': """A cave with this name already exists.
                 Please choose another name.""",
                'max_lenght': "Cave name must not exceed 40 characters.",
            },
            "latitude": {
                'required': "Latitude is a required field.",
                'invalid': """Please adhere exactly format as shown
                 in the example."""
            },
            "longitude": {
                'required': "Longitude is a required field.",
                'invalid': """Please adhere exactly format as shown
                 in the example."""
            },
            "length": {
                'required': "Lenght is a required field.",
                'invalid': """Please adhere exactly format as shown
                 in the example."""
            },
            "depth": {
                'required': "Depth is a required field.",
                'invalid': """Please adhere exactly format as shown
                 in the example."""
            },
            "area": {
                'required': "Area is a required field.",
                'invalid': """Please adhere exactly format as shown
                 in the example."""
            },
            "volume": {
                'required': "Volume is a required field.",
                'invalid': """Please adhere exactly format as shown
                 in the example."""
            },
            "cave_map": {
                'invalid': "Something went wrong, please try again."
            },
        }

        widgets = {
            'user': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'rows': 10, 'cols': 15}),
        }
