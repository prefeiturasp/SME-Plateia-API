from django.db import models
from general.models import City
from user.models import User

class Comment(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    showid = models.ForeignKey('Show', models.DO_NOTHING, db_column='ShowId')  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=500)  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Comment'
        
class Genre(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Genre'


class Genreshowtype(models.Model):
    genreid = models.OneToOneField(Genre, models.DO_NOTHING, db_column='GenreId', primary_key=True)  # Field name made lowercase.
    showtypeid = models.ForeignKey('Showtype', models.DO_NOTHING, db_column='ShowTypeId')  # Field name made lowercase.

    class Meta:
        
        db_table = 'GenreShowType'
        unique_together = (('genreid', 'showtypeid'),)


class File(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=300)  # Field name made lowercase.
    length = models.IntegerField(db_column='Length')  # Field name made lowercase.
    path = models.TextField(db_column='Path')  # Field name made lowercase.
    thumbnailpath = models.TextField(db_column='ThumbnailPath', blank=True, null=True)  # Field name made lowercase.
    extension = models.TextField(db_column='Extension', blank=True, null=True)  # Field name made lowercase.
    showid = models.ForeignKey('Show', models.DO_NOTHING, db_column='ShowId')  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'File'


class Show(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    synopsis = models.CharField(db_column='Synopsis', max_length=1500)  # Field name made lowercase.
    classification = models.CharField(db_column='Classification', max_length=150, blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration')  # Field name made lowercase.
    postscript = models.CharField(db_column='PostScript', max_length=250, blank=True, null=True)  # Field name made lowercase.
    video = models.CharField(db_column='Video', max_length=150, blank=True, null=True)  # Field name made lowercase.
    showtypeid = models.ForeignKey('Showtype', models.DO_NOTHING, db_column='ShowTypeId')  # Field name made lowercase.
    genreid = models.ForeignKey(Genre, models.DO_NOTHING, db_column='GenreId')  # Field name made lowercase.
    highlight = models.SmallIntegerField(db_column='HighLight', blank=True, null=True)  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Show'


class Showtype(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'ShowType'


class Event(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    showid = models.ForeignKey('Show', models.DO_NOTHING, db_column='ShowId')  # Field name made lowercase.
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='CityId')  # Field name made lowercase.
    local = models.CharField(db_column='Local', max_length=300)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=400)  # Field name made lowercase.
    partnercompany = models.CharField(db_column='PartnerCompany', max_length=150, blank=True, null=True)  # Field name made lowercase.
    presentationdate = models.DateTimeField(db_column='PresentationDate')  # Field name made lowercase.
    schedule = models.DateTimeField(db_column='Schedule')  # Field name made lowercase.
    enrollstartat = models.DateTimeField(db_column='EnrollStartAt')  # Field name made lowercase.
    enrollendat = models.DateTimeField(db_column='EnrollEndAt')  # Field name made lowercase.
    ticketquantity = models.IntegerField(db_column='TicketQuantity')  # Field name made lowercase.
    ticketavailable = models.IntegerField(db_column='TicketAvailable')  # Field name made lowercase.
    ticketbymember = models.IntegerField(db_column='TicketByMember')  # Field name made lowercase.
    queuesize = models.IntegerField(db_column='QueueSize')  # Field name made lowercase.
    queueremaining = models.IntegerField(db_column='QueueRemaining')  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Event'        



class Eventhistory(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    showid = models.BigIntegerField(db_column='ShowId', blank=True, null=True)  # Field name made lowercase.
    cityid = models.CharField(db_column='CityId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    local = models.CharField(db_column='Local', max_length=300, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=400, blank=True, null=True)  # Field name made lowercase.
    partnercompany = models.CharField(db_column='PartnerCompany', max_length=150, blank=True, null=True)  # Field name made lowercase.
    presentationdate = models.DateTimeField(db_column='PresentationDate', blank=True, null=True)  # Field name made lowercase.
    schedule = models.DateTimeField(db_column='Schedule', blank=True, null=True)  # Field name made lowercase.
    enrollstartat = models.DateTimeField(db_column='EnrollStartAt', blank=True, null=True)  # Field name made lowercase.
    enrollendat = models.DateTimeField(db_column='EnrollEndAt', blank=True, null=True)  # Field name made lowercase.
    ticketquantity = models.IntegerField(db_column='TicketQuantity', blank=True, null=True)  # Field name made lowercase.
    ticketavailable = models.IntegerField(db_column='TicketAvailable', blank=True, null=True)  # Field name made lowercase.
    ticketbymember = models.IntegerField(db_column='TicketByMember', blank=True, null=True)  # Field name made lowercase.
    queuesize = models.IntegerField(db_column='QueueSize', blank=True, null=True)  # Field name made lowercase.
    queueremaining = models.IntegerField(db_column='QueueRemaining', blank=True, null=True)  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = '_EventHistory'
