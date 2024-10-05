from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Tasks(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)          
    title= models.CharField(max_length=200)
    description= models.TextField(null=True,
                               blank=True)
    
    due_date = models.DateTimeField(default=timezone.now)
    priority = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'), (3, 'High')), default=1)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
"""class Image(models.Model):
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE,related_name='images',verbose_name=('image'), blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=False, null=True)
    
    def __str__(self):
        return str(self.image)

    def save( self, *args, **kwargs):
        
        super(Image, self).save(*args, **kwargs)"""



class FeedFile(models.Model):
    image = models.ImageField(upload_to="images", blank=False, null=True)
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE,related_name='images',verbose_name=('image'), blank=True, null=True)