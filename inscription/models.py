from django.db import models
from event.models import Event
from user.models import User

class Inscription(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    eventid = models.ForeignKey(Event, models.DO_NOTHING, db_column='EventId')  # Field name made lowercase.
    presence = models.BooleanField(db_column='Presence')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority')  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Inscription'
