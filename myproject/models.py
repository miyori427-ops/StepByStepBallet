
from datetime import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 必要なカスタムフィールドを追加
    phone_number = models.CharField(max_length=15, null=True, blank=True)



