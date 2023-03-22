# Generated by Django 4.1.3 on 2023-03-22 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='userid',
            field=models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
