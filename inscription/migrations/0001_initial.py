# Generated by Django 4.1.3 on 2023-03-22 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presence', models.BooleanField(db_column='Presence')),
                ('priority', models.IntegerField(db_column='Priority')),
                ('state', models.SmallIntegerField(db_column='State')),
                ('createdate', models.DateTimeField(db_column='CreateDate')),
                ('updatedate', models.DateTimeField(db_column='UpdateDate')),
                ('eventid', models.ForeignKey(db_column='EventId', on_delete=django.db.models.deletion.DO_NOTHING, to='event.event')),
            ],
        ),
    ]