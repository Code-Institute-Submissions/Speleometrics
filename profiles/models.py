from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_resized import ResizedImageField
from cloudinary.models import CloudinaryField

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
    display_name = models.CharField(max_length=40, blank=False)
    email_for_contact = models.EmailField(max_length=100, blank=False)
    profile_type = models.IntegerField(choices=USER_TYPE,default=0, blank=False)
    bio = models.TextField(blank=True)
    image = ResizedImageField(size=[300, 300], quality=75, upload_to="profiles/",
     force_format='WEBP', blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name="user_profile")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates a profile for a new user.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Creates a profile for a user created before profile app.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
