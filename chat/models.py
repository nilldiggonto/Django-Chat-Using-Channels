from django.db import models
from django.utils.text import slugify

# Create your models here.
class ChatRoom(models.Model):
    name        = models.CharField(max_length=255)
    slug        = models.SlugField(unique=True,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    active      = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(ChatRoom, self).save(*args, **kwargs)    
    def __str__(self):
        return self.name