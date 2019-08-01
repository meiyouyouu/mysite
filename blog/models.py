from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
class BlogArticles(models.Model):
    title =models.CharField(max_length=300)
    author = models.ForeignKey(User,related_name="blog_posts",on_delete='CASCADE')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title