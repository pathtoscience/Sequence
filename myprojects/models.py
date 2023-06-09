from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    
    def __str__(self):
        return self.title