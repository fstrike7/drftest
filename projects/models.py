from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(default="https://assets.streamlinehq.com/image/private/w_300,h_300,ar_1/f_auto/v1/icons/photo-image/broken-image-yqwggbcj8soxi4blx8k2di.png/broken-image-0hrbdnmxhic4dti6bv0wu57.png?_a=DAJFJtWIZAAC")
    technologies = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)