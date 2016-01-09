# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20160107_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergetlist',
            name='phone_no',
            field=models.CharField(help_text=b'Ex: 8050459876', max_length=10, null=True, verbose_name=b'Phone', blank=True),
        ),
        migrations.AlterField(
            model_name='usergetlist',
            name='website',
            field=models.URLField(help_text=b'Ex:http://www.example.com', verbose_name=b'Website', blank=True),
        ),
    ]
