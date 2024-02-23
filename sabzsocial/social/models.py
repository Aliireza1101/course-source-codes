from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(verbose_name="بیوگرافی", blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="تاریخ تولد", blank=True, null=True)
    photo = models.ImageField(verbose_name="عکس پروفایل", upload_to="profiles", blank=True, null=True)
    job = models.CharField(verbose_name="شغل", max_length=255, blank=True, null=True)
    phone = models.CharField(verbose_name="شماره تلفن", max_length=11, blank=True, null=True)

