from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password=password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)


class User(AbstractBaseUser):
    USERNAME_FIELD = 'login'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ["email"]

    id = models.CharField(db_column='Id', primary_key=True, max_length=36) 
    entityid = models.CharField(db_column='EntityId', max_length=36) 
    login = models.CharField(db_column='Login', max_length=500, blank=True, null=True) 
    crypt = models.CharField(db_column='Crypt', max_length=128) 
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True) 
    rf = models.CharField(db_column='RF', max_length=25, blank=True, null=True) 
    email = models.EmailField(db_column='Email', blank=True, null=True) 
    tel = models.TextField(db_column='Tel', blank=True, null=True) 
    isadmin = models.BooleanField(db_column='IsAdmin') 
    eventduedate = models.DateTimeField(db_column='EventDueDate', blank=True, null=True) 
    punishmentduedate = models.DateTimeField(db_column='PunishmentDueDate', blank=True, null=True) 
    state = models.SmallIntegerField(db_column='State') 
    createdate = models.DateTimeField(db_column='CreateDate') 
    updatedate = models.DateTimeField(db_column='UpdateDate') 

    objects = CustomUserManager()

    class Meta:
        db_table = 'User'
