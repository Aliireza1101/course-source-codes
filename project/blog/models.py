from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.utils import timezone


# Create your managers here.
class PostPublishManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Post.Status.published)


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

    # Managers :
    objects = models.Manager()
    published = PostPublishManager()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ("-publish_date",)
        indexes = [models.Index(fields=["-publish_date",])]