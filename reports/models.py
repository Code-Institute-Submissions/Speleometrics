from django.db import models
from django.db import models
from django.contrib.auth.models import User
from caves.models import Cave

# Create your models here.

class Report(models.Model):
    reported_by = models.ForeignKey(User, related_name='reported_by_user', on_delete=models.CASCADE)
    cave = models.ForeignKey(Cave, related_name='reported_cave', on_delete=models.CASCADE)
    cave_owner = models.ForeignKey(User, related_name='cave_owner_user', on_delete=models.CASCADE)
    inconsistency_details = models.TextField()
    reported_created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{ self.cave.cave_name }, owned by { 
            self.cave.cave_owner.username } reported by {
              self.reported_by.username  
            }'