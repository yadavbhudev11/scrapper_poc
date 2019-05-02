from django.db import models
#from django.urls import reverse
#from django.utils import timezone
#from django.contrib.auth.models import User


class Notif(models.Model):
    
    title = models.CharField(max_length=500,
                             unique_for_date='publish')
    
    link = models.CharField(max_length=1000)
    
    publish = models.DateTimeField(null=True, blank=True)
    
    info = models.TextField()
    
    
class Meta:
    ordering = ('-publish',)


