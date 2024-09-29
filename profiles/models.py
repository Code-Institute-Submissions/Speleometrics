from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    email_for_contact = models.EmailField(max_length=100, blank=False)
    profile_type = models.IntegerField(choices=USER_TYPE, 
        default=0, blank=False)
    bio = models.TextField(blank=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name="user_profile"
    )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()