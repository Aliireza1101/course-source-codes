from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        published = "PB", "Published"
        rejected = "RJ", "Rejected"
        drafted = "DR", "Drafted"

    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="posts"
    )
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.drafted)

    publish_date = models.DateTimeField(default=timezone.now)
    create_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ("-publish_date",)
        indexes = [models.Index(fields=["-publish_date",])]
