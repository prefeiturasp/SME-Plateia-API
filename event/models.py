from django.db import models
from general.models import City
from user.models import User


class Comment(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    userid = models.ForeignKey(User, models.DO_NOTHING, to_field='id', db_column='UserId')
    showid = models.ForeignKey('Show', models.DO_NOTHING, to_field='id', db_column='ShowId')
    content = models.CharField(db_column='Content', max_length=500)
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        db_table = 'Comment'
        managed = False


class Genre(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    name = models.CharField(db_column='Name', max_length=150)
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        db_table = 'Genre'
        managed = False


class Genreshowtype(models.Model):
    genreid = models.OneToOneField(Genre, models.DO_NOTHING, db_column='GenreId', primary_key=True)
    showtypeid = models.ForeignKey('Showtype', models.DO_NOTHING, to_field='id', db_column='ShowTypeId')

    class Meta:
        db_table = 'Genreshowtype'
        unique_together = (('genreid', 'showtypeid'),)
        managed = False


class File(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    name = models.CharField(db_column='Name', max_length=300)
    length = models.IntegerField(db_column='Length')
    path = models.TextField(db_column='Path')
    thumbnailpath = models.TextField(db_column='ThumbnailPath', blank=True, null=True)
    extension = models.TextField(db_column='Extension', blank=True, null=True)
    showid = models.ForeignKey('Show', models.DO_NOTHING, to_field='id', db_column='ShowId')
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        db_table = 'File'
        managed = False


class Show(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    name = models.CharField(db_column='Name', max_length=150)
    synopsis = models.CharField(db_column='Synopsis', max_length=1500)
    classification = models.CharField(db_column='Classification', max_length=150, blank=True, null=True)
    duration = models.IntegerField(db_column='Duration')
    postscript = models.CharField(db_column='PostScript', max_length=250, blank=True, null=True)
    video = models.CharField(db_column='Video', max_length=150, blank=True, null=True)
    showtypeid = models.ForeignKey('Showtype', models.DO_NOTHING, to_field='id', db_column='ShowTypeId')
    genreid = models.ForeignKey(Genre, models.DO_NOTHING, to_field='id', db_column='GenreId')
    highlight = models.SmallIntegerField(db_column='HighLight', blank=True, null=True)
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        db_table = 'Show'
        managed = False


class Showtype(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    name = models.CharField(db_column='Name', max_length=150)
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        db_table = 'ShowType'
        managed = False


class Event(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    showid = models.ForeignKey('Show', models.DO_NOTHING, to_field='id', db_column='ShowId')
    cityid = models.ForeignKey(City, models.DO_NOTHING, to_field='id', db_column='CityId')
    local = models.CharField(db_column='Local', max_length=300)
    address = models.CharField(db_column='Address', max_length=400)
    partnercompany = models.CharField(db_column='PartnerCompany', max_length=150, blank=True, null=True)
    presentationdate = models.DateTimeField(db_column='PresentationDate')
    schedule = models.DateTimeField(db_column='Schedule')
    enrollstartat = models.DateTimeField(db_column='EnrollStartAt')
    enrollendat = models.DateTimeField(db_column='EnrollEndAt')
    ticketquantity = models.IntegerField(db_column='TicketQuantity')
    ticketavailable = models.IntegerField(db_column='TicketAvailable')
    ticketbymember = models.IntegerField(db_column='TicketByMember')
    queuesize = models.IntegerField(db_column='QueueSize')
    queueremaining = models.IntegerField(db_column='QueueRemaining')
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        db_table = 'Event'
        managed = False


class Eventhistory(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    showid = models.BigIntegerField(db_column='ShowId', blank=True, null=True)
    cityid = models.CharField(db_column='CityId', max_length=36, blank=True, null=True)
    local = models.CharField(db_column='Local', max_length=300, blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=400, blank=True, null=True)
    partnercompany = models.CharField(db_column='PartnerCompany', max_length=150, blank=True, null=True)
    presentationdate = models.DateTimeField(db_column='PresentationDate', blank=True, null=True)
    schedule = models.DateTimeField(db_column='Schedule', blank=True, null=True)
    enrollstartat = models.DateTimeField(db_column='EnrollStartAt', blank=True, null=True)
    enrollendat = models.DateTimeField(db_column='EnrollEndAt', blank=True, null=True)
    ticketquantity = models.IntegerField(db_column='TicketQuantity', blank=True, null=True)
    ticketavailable = models.IntegerField(db_column='TicketAvailable', blank=True, null=True)
    ticketbymember = models.IntegerField(db_column='TicketByMember', blank=True, null=True)
    queuesize = models.IntegerField(db_column='QueueSize', blank=True, null=True)
    queueremaining = models.IntegerField(db_column='QueueRemaining', blank=True, null=True)
    state = models.SmallIntegerField(db_column='State', blank=True, null=True)
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)

    class Meta:
        db_table = '_EventHistory'
        managed = False
