# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_questionpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionpost',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='questionpost',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 18, 11, 22, 24, 246313, tzinfo=utc)),
        ),
    ]
