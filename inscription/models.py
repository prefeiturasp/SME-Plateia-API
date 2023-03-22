from django.db import models
from event.models import Event
from user.models import User


class Inscription(models.Model):

    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserId')
    eventid = models.ForeignKey(Event, models.DO_NOTHING, db_column='EventId')
    presence = models.BooleanField(db_column='Presence')
    priority = models.IntegerField(db_column='Priority')
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')
