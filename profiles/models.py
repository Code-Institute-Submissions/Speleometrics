from django.db import models
from django.contrib.auth.models import User

# Create your models here.

USER_TYPE = (
    (0, "Academic"),
    (2, "Company"),
    (3, "Professional Speleologist"),
    (4, "Speleology Enthusiast"),
    (5, "Governmental Agency"),
)

class Profile(models.Model):
    """
    Add profile info for the user.
    """
    email_contact = models.EmailField(max_length=100, blank=False)
    profile_type = models.IntegerField(choices=USER_TYPE, 
        default=0, blank=False)
    bio = models.TextField(blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_profile"
    )