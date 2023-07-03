from django.db import models
from django.conf import settings
from django.db.models import Q
from general.models import City
from user.models import User


class Comment(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, to_field='id', db_column='UserId')
    showid = models.ForeignKey('Show', models.DO_NOTHING, db_column='ShowId')
    content = models.CharField(db_column='Content', max_length=500)
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        db_table = 'Comment'
        managed = False


class Genre(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
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
        db_table = 'GenreShowType'
        unique_together = (('genreid', 'showtypeid'),)
        managed = False


class File(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=300)
    length = models.IntegerField(db_column='Length')
    path = models.TextField(db_column='Path')
    thumbnailpath = models.TextField(db_column='ThumbnailPath', blank=True, null=True)
    extension = models.TextField(db_column='Extension', blank=True, null=True)
    showid = models.ForeignKey('Show', models.DO_NOTHING, db_column='ShowId')
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        db_table = 'File'
        managed = False

    @staticmethod
    def get_full_file_path(path: str):
        return settings.BASE_MEDIA_EXTERNAL_PATH + path


class Show(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
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
    id = models.BigAutoField(db_column='Id', primary_key=True)
    name = models.CharField(db_column='Name', max_length=150)
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        db_table = 'ShowType'
        managed = False


class Event(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
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

    @staticmethod
    def get_events_by_user_and_dates(user_id: str, start_date: str, end_date: str = None, previous_queryset=None):
        """
        Retorna um QuerySet com os eventos em que um determinado usuário está inscrito e que ocorrem
        entre as datas de início e fim especificadas.

        :param user_id: ID do usuário
        :param start_date: Data de início no formato "YYYY-MM-DD HH:MM:SS"
        :param end_date: Data de fim no formato "YYYY-MM-DD HH:MM:SS"
        :param previous_queryset: Queryset para somar no filtro.
        :return: QuerySet com os eventos
        """

        if end_date:
            query = f"""
                SELECT
                    "Event"."Schedule",
                    "Event"."Id",
                    "Event"."ShowId",
                    "Event"."CityId",
                    "Event"."Local",
                    "Event"."Address",
                    "Event"."PartnerCompany",
                    "Event"."PresentationDate",
                    "Event"."Schedule",
                    "Event"."EnrollStartAt",
                    "Event"."EnrollEndAt",
                    "Event"."TicketQuantity",
                    "Event"."TicketAvailable",
                    "Event"."TicketByMember",
                    "Event"."QueueSize",
                    "Event"."QueueRemaining",
                    "Event"."State",
                    "Event"."CreateDate",
                    "Event"."UpdateDate"
                FROM
                    "Event"
                INNER JOIN
                    "Inscription" ON ("Event"."Id" = "Inscription"."EventId")
                WHERE
                    ("Inscription"."UserId" = '{user_id}')
                    AND (("Event"."Schedule" >= to_timestamp('{start_date}', 'YYYY-MM-DD HH24:MI:SS')
                        AND "Event"."Schedule" <= to_timestamp('{end_date}', 'YYYY-MM-DD HH24:MI:SS'))
                        OR ("Event"."PresentationDate" >= to_timestamp('{start_date}', 'YYYY-MM-DD HH24:MI:SS')
                            AND "Event"."PresentationDate" <= to_timestamp('{end_date}', 'YYYY-MM-DD HH24:MI:SS')))
            """
        else:
            query = f"""
                SELECT
                    "Event"."Schedule",
                    "Event"."Id",
                    "Event"."ShowId",
                    "Event"."CityId",
                    "Event"."Local",
                    "Event"."Address",
                    "Event"."PartnerCompany",
                    "Event"."PresentationDate",
                    "Event"."Schedule",
                    "Event"."EnrollStartAt",
                    "Event"."EnrollEndAt",
                    "Event"."TicketQuantity",
                    "Event"."TicketAvailable",
                    "Event"."TicketByMember",
                    "Event"."QueueSize",
                    "Event"."QueueRemaining",
                    "Event"."State",
                    "Event"."CreateDate",
                    "Event"."UpdateDate"
                FROM
                    "Event"
                INNER JOIN
                    "Inscription" ON ("Event"."Id" = "Inscription"."EventId")
                WHERE
                    ("Inscription"."UserId" = '{user_id}')
                    AND ("Event"."Schedule" >= to_timestamp('{start_date}', 'YYYY-MM-DD HH24:MI:SS')
                        OR "Event"."PresentationDate" >= to_timestamp('{start_date}', 'YYYY-MM-DD HH24:MI:SS'))
            """
        raw_queryset = Event.objects.raw(query)

        if previous_queryset:
            queryset = previous_queryset.filter(Q(id__in=[item.id for item in raw_queryset]))
        else:
            queryset = Event.objects.filter(Q(id__in=[item.id for item in raw_queryset]))

        return queryset

    @staticmethod
    def get_events_by_dates(start_date: str, end_date: str = None, previous_queryset=None):
        """
        Retorna um QuerySet com os eventos em que um determinado usuário está inscrito e que ocorrem
        entre as datas de início e fim especificadas.

        :param user_id: ID do usuário
        :param start_date: Data de início no formato "YYYY-MM-DD HH:MM:SS"
        :param end_date: Data de fim no formato "YYYY-MM-DD HH:MM:SS"
        :param previous_queryset: Queryset para somar no filtro.
        :return: QuerySet com os eventos
        """

        query = f"""
            SELECT
                "Event"."Schedule",
                "Event"."Id",
                "Event"."ShowId",
                "Event"."CityId",
                "Event"."Local",
                "Event"."Address",
                "Event"."PartnerCompany",
                "Event"."PresentationDate",
                "Event"."Schedule",
                "Event"."EnrollStartAt",
                "Event"."EnrollEndAt",
                "Event"."TicketQuantity",
                "Event"."TicketAvailable",
                "Event"."TicketByMember",
                "Event"."QueueSize",
                "Event"."QueueRemaining",
                "Event"."State",
                "Event"."CreateDate",
                "Event"."UpdateDate"
            FROM
                "Event"
            INNER JOIN
                "Inscription" ON ("Event"."Id" = "Inscription"."EventId")
            WHERE
                ("Event"."EnrollStartAt" >= to_timestamp('{start_date}', 'YYYY-MM-DD HH24:MI:SS')
                AND "Event"."EnrollEndAt" <= to_timestamp('{end_date}', 'YYYY-MM-DD HH24:MI:SS'))
                AND (("Event"."Schedule" >= to_timestamp('{start_date}', 'YYYY-MM-DD HH24:MI:SS')
                    AND "Event"."Schedule" <= to_timestamp('{end_date}', 'YYYY-MM-DD HH24:MI:SS'))
                    OR ("Event"."PresentationDate" >= to_timestamp('{start_date}', 'YYYY-MM-DD HH24:MI:SS')
                        AND "Event"."PresentationDate" <= to_timestamp('{end_date}', 'YYYY-MM-DD HH24:MI:SS')))
        """
        raw_queryset = Event.objects.raw(query)

        if previous_queryset:
            queryset = previous_queryset.filter(Q(id__in=[item.id for item in raw_queryset]))
        else:
            queryset = Event.objects.filter(Q(id__in=[item.id for item in raw_queryset]))

        return queryset


class Eventhistory(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)
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
