from django.db import models 
from django.contrib.auth import get_user_model 
User = get_user_model()
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # 衝突を避けるために変更
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # 衝突を避けるために変更
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='customuser',
    )
