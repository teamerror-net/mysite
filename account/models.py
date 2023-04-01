from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from account.managers import UserManager
# Create your models here.
class Users(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name_plural ="All User"
    username = models.CharField(verbose_name='Username',max_length=20,unique=True,editable=False)
    absent = models.CharField(verbose_name='Absent',max_length=200,default=0)
    present = models.CharField(verbose_name='Present',max_length=200,default=0)
    user_level =(
        ('1','Male'),
        ('2','Female'),
    )
    gender = models.CharField(max_length=20, choices=user_level, default='1')
    account_open = models.CharField(verbose_name='Account Open',max_length=200,default=0)
    account_open_time = models.CharField(verbose_name='Time',max_length=200,default=0)
    is_active = models.BooleanField(verbose_name='Active',default=True)
    is_staff = models.BooleanField(verbose_name='Staff',default=False)
    is_superuser = models.BooleanField(verbose_name='Superuser',default=False)
    is_signin = models.BooleanField(verbose_name='Today Status',default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True