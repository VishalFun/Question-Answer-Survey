# Generated by Django 3.0.5 on 2020-08-16 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
