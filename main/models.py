from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    
    def publish(self):
        self.published_date = timezone.now()
        self.is_published = True
        self.save()
    
    def __str__(self):
        return self.title
