from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    entityid = models.CharField(db_column='EntityId', max_length=36)
    login = models.CharField(db_column='Login', max_length=500, blank=True, null=True)
    crypt = models.CharField(db_column='Crypt', max_length=128)
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)
    rf = models.CharField(db_column='RF', max_length=25, blank=True, null=True)
    email = models.EmailField(db_column='Email', blank=True, null=True)
    tel = models.TextField(db_column='Tel', blank=True, null=True)
    isadmin = models.BooleanField(db_column='IsAdmin', default=False)
    eventduedate = models.DateTimeField(db_column='EventDueDate', blank=True, null=True)
    punishmentduedate = models.DateTimeField(db_column='PunishmentDueDate', blank=True, null=True)
    state = models.SmallIntegerField(db_column='State', blank=True, null=True)
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)
