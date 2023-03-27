from django.db import models


class City(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    name = models.CharField(db_column='Name', max_length=200)
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        managed = False


class Logactivity(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    date = models.DateTimeField(db_column='Date')
    message = models.CharField(db_column='Message', max_length=4000, blank=True, null=True)
    action = models.CharField(db_column='Action', max_length=30, blank=True, null=True)
    browser = models.CharField(db_column='Browser', max_length=250, blank=True, null=True)
    hostname = models.CharField(db_column='HostName', max_length=500, blank=True, null=True)
    userhostaddress = models.CharField(db_column='UserHostAddress', max_length=500, blank=True, null=True)
    querystring = models.CharField(db_column='QueryString', max_length=500, blank=True, null=True)
    filepath = models.CharField(db_column='FilePath', max_length=250, blank=True, null=True)
    identity = models.CharField(db_column='Identity', max_length=250, blank=True, null=True)
    plataform = models.CharField(db_column='Plataform', max_length=250, blank=True, null=True)
    mobiledevicemodel = models.CharField(db_column='MobileDeviceModel', max_length=250, blank=True, null=True)

    class Meta:
        managed = False


class Logerror(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    date = models.DateTimeField(db_column='Date')
    level = models.CharField(db_column='Level', max_length=50, blank=True, null=True)
    logger = models.CharField(db_column='Logger', max_length=255, blank=True, null=True)
    message = models.CharField(db_column='Message', max_length=4000, blank=True, null=True)
    exception = models.CharField(db_column='Exception', max_length=8000, blank=True, null=True)
    browser = models.CharField(db_column='Browser', max_length=250, blank=True, null=True)
    hostname = models.CharField(db_column='HostName', max_length=500, blank=True, null=True)
    userhostaddress = models.CharField(db_column='UserHostAddress', max_length=500, blank=True, null=True)
    querystring = models.CharField(db_column='QueryString', max_length=500, blank=True, null=True)
    filepath = models.CharField(db_column='FilePath', max_length=250, blank=True, null=True)
    identity = models.CharField(db_column='Identity', max_length=250, blank=True, null=True)
    plataform = models.CharField(db_column='Plataform', max_length=250, blank=True, null=True)
    mobiledevicemodel = models.CharField(db_column='MobileDeviceModel', max_length=250, blank=True, null=True)

    class Meta:
        managed = False


class Parameter(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)
    key = models.CharField(db_column='Key', max_length=100)
    value = models.CharField(db_column='Value', max_length=250, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=250)
    state = models.SmallIntegerField(db_column='State')
    createdate = models.DateTimeField(db_column='CreateDate')
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        managed = False
