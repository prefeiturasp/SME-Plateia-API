from django.db import models

class City(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'City'


class Logactivity(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=30, blank=True, null=True)  # Field name made lowercase.
    browser = models.CharField(db_column='Browser', max_length=250, blank=True, null=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='HostName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    userhostaddress = models.CharField(db_column='UserHostAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    querystring = models.CharField(db_column='QueryString', max_length=500, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=250, blank=True, null=True)  # Field name made lowercase.
    identity = models.CharField(db_column='Identity', max_length=250, blank=True, null=True)  # Field name made lowercase.
    plataform = models.CharField(db_column='Plataform', max_length=250, blank=True, null=True)  # Field name made lowercase.
    mobiledevicemodel = models.CharField(db_column='MobileDeviceModel', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'LogActivity'


class Logerror(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=50, blank=True, null=True)  # Field name made lowercase.
    logger = models.CharField(db_column='Logger', max_length=255, blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    exception = models.CharField(db_column='Exception', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    browser = models.CharField(db_column='Browser', max_length=250, blank=True, null=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='HostName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    userhostaddress = models.CharField(db_column='UserHostAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    querystring = models.CharField(db_column='QueryString', max_length=500, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=250, blank=True, null=True)  # Field name made lowercase.
    identity = models.CharField(db_column='Identity', max_length=250, blank=True, null=True)  # Field name made lowercase.
    plataform = models.CharField(db_column='Plataform', max_length=250, blank=True, null=True)  # Field name made lowercase.
    mobiledevicemodel = models.CharField(db_column='MobileDeviceModel', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'LogError'


class Parameter(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    key = models.CharField(db_column='Key', max_length=100)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=250, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=250)  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Parameter'