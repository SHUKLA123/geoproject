from django.db import models
from django.contrib.auth.models import User
class shape_data(models.Model):
    north = models.FloatField()
    south = models.FloatField()
    east = models.FloatField()
    west = models.FloatField()
    
