# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20161118_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionpost',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 18, 11, 24, 7, 558646, tzinfo=utc)),
        ),
    ]
