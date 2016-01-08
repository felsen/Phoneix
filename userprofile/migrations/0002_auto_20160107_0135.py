# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergetlist',
            name='phone_no',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Phone', blank=True),
        ),
    ]
