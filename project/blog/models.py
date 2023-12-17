from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


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
    update_date = models.DateTimeField(auto_now=True)

    # Managers :
    objects = models.Manager()
    published = PostPublishManager()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ("-publish_date",)
        indexes = [models.Index(fields=["-publish_date",])]
        # verbose_name = "پست"
        # verbose_name_plural = "پست ها"


    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.id})
    

class Ticket(models.Model):
    class Subject(models.TextChoices):
        proposal = "PP", "Proposal"
        feedback = "FB", "Feedback"
        report = "RP", "Report"

    title = models.CharField(max_length=255)
    message = models.TextField()

    subject = models.CharField(max_length=2, choices=Subject.choices)
    
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "تیکت"
        verbose_name_plural = "تیکت ها"
