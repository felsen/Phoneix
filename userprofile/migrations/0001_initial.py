# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserGetList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=50, verbose_name=b'Name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email', blank=True)),
                ('phone_no', models.IntegerField(null=True, verbose_name=b'Phone', blank=True)),
                ('organization_name', models.CharField(max_length=50, verbose_name=b'Organization Name', blank=True)),
                ('address', models.TextField(max_length=750, null=True, verbose_name=b'Address', blank=True)),
                ('website', models.URLField(verbose_name=b'Website', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
