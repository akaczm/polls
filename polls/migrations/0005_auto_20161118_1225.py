# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20161118_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionpost',
            name='content',
            field=models.TextField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='questionpost',
            name='post_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
