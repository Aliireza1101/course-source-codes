from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django_resized import ResizedImageField
from django.core.files.storage import default_storage
from django.template.defaultfilters import slugify


# Create your managers here.
class PostPublishManager(models.Manager): # Manager to get only published posts
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Post.Status.published)


class CommentActiveManager(models.Manager): # Manager to get only active comments
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_active=True)


# Create your models here.
class Post(models.Model): # Posts
    class Status(models.TextChoices):
        published = "PB", "Published"
        rejected = "RJ", "Rejected"
        drafted = "DR", "Drafted"

    class Category(models.TextChoices):
        TECHNOLOGY = "Tech", "Technology"
        PROGRAMMING = "Programming", "Programming"
        NETWORK = "Network", "Network"
        IT = "IT", "Information Technology"
        AI = "AI", "Artificial Intelligence"
        OTHERS = "Others", "Others"

    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.drafted
    )

    reading_time = models.PositiveIntegerField()

    publish_date = models.DateTimeField(default=timezone.now)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    category = models.CharField(
        max_length=255, choices=Category.choices, default=Category.OTHERS
    )

    # Managers :
    objects = models.Manager()
    published = PostPublishManager()

    def __str__(self) -> str:
        return self.title

    def delete(self, *args, **kwargs):
        for image in self.images.all():
            if image:
                default_storage.delete(image.image_file.path)
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ("-publish_date",)
        indexes = [
            models.Index(
                fields=[
                    "-publish_date",
                ]
            )
        ]
        # verbose_name = "پست"
        # verbose_name_plural = "پست ها"

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.id})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(args, kwargs)


class Ticket(models.Model): # Tickets
    class Subject(models.TextChoices):
        proposal = "PP", "Proposal"
        feedback = "FB", "Feedback"
        report = "RP", "Report"

    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="tickets"
    )

    title = models.CharField(max_length=255)
    message = models.TextField()

    subject = models.CharField(max_length=2, choices=Subject.choices)

    email = models.EmailField()
    phone_number = models.CharField(max_length=11)

    active = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    # class Meta:
    #     verbose_name = "تیکت"
    #     verbose_name_plural = "تیکت ها"


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    # Managers :
    objects = models.Manager()
    actives = CommentActiveManager()

    def __str__(self) -> str:
        return " ".join(self.text.split()[:5]) + "..."

    class Meta:
        ordering = ("-create_date",)
        indexes = [
            models.Index(
                fields=[
                    "-create_date",
                ]
            )
        ]
        # verbose_name = "کامنت"
        # verbose_name_plural = "کامنت ها"


class Image(models.Model): # Images
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="images")
    image_file = ResizedImageField(
        size=[500, 500],
        upload_to="images/posts/%Y/%m",
        quality=100,
        crop=["middle", "center"],
    )

    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        if not self.title:
            name: str = self.image_file.name.split("/")[-1]
            return name
        return self.title

    def delete(self, *args, **kwargs):
        default_storage.delete(self.image_file.path)
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ("-create_date",)
        indexes = [
            models.Index(
                fields=[
                    "-create_date",
                ]
            )
        ]
        # verbose_name = "تصویر"
        # verbose_name_plural = "تصویر ها"


class Account(models.Model): # User's account
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField()
    photo = ResizedImageField(
        size=[500, 500],
        upload_to="images/profiles/",
        quality=60,
        crop=["middle", "center"],
    )
    job = models.CharField(max_length=255)

    # class Meta:
    #     verbose_name = "اکانت"
    #     verbose_name_plural = "اکانت ها"
