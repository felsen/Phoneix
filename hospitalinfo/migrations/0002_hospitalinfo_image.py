# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalinfo',
            name='image',
            field=models.ImageField(default=b'static/img/icons_healthcare.png', upload_to=b'static/%Y_%m_%d/'),
        ),
    ]
