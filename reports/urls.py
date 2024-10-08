from django.db import models
from django.db import models
from django.contrib.auth.models import User
from caves.models import Cave

class Report(models.Model):
    reported_by = models.ForeignKey(User, related_name='reports_made', on_delete=models.CASCADE)
    cave = models.ForeignKey(Cave, related_name='reports_cave', on_delete=models.CASCADE)
    cave_owner = models.ForeignKey(User, related_name='reports_made', on_delete=models.CASCADE)
    inconsistency_details = models.TextField()
    reported_created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{ self.cave.cave_name }, owned by { 
            self.cave.cave_owner.username } reported by {
              self.reported_by.username  
            }'