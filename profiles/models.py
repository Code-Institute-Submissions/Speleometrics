from django.db import models

# Create your models here.

class Profile(models.Model):
    """
    Add profile info for the user.
    """
    email_contact = models.EmailField(max_length=100)
    profile_type = models.IntegerField(choices=USER_TYPE, 
        default=0, blank=False)
    bio = models.TextField(blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_profile"
    )