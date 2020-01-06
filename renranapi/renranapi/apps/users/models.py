from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号码")
    avatar = models.ImageField(null=True, blank=True, verbose_name="用户头像")

    class Meta:
        db_table = "rr_users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name
