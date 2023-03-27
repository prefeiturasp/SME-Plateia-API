from django.db import models
from django.contrib.auth.hashers import (
    check_password,
    make_password,
)


class User(models.Model):
    id = models.SlugField(db_column='Id', primary_key=True, max_length=36)
    entityid = models.CharField(db_column='EntityId', max_length=36)
    login = models.CharField(db_column='Login', max_length=500, blank=True, null=True)
    password = models.CharField(db_column="Password", max_length=128)
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

    class Meta:
        db_table = 'User'
        managed = False

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        return super(User, self).save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """

        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)
