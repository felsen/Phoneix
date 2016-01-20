# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalinfo', '0002_hospitalinfo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('spacility', models.TextField(max_length=100)),
                ('image', models.ImageField(default=b'static/img/icons_healthcare.png', upload_to=b'static/%Y_%m_%d/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DgLabsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('spacility', models.TextField(max_length=100)),
                ('image', models.ImageField(default=b'static/img/icons_healthcare.png', upload_to=b'static/%Y_%m_%d/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DoctorsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('spacility', models.TextField(max_length=100)),
                ('image', models.ImageField(default=b'static/admin_static/dist/img/pic.jpg', upload_to=b'static/%Y_%m_%d/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PharmacyInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('spacility', models.TextField(max_length=100)),
                ('image', models.ImageField(default=b'static/img/icons_healthcare.png', upload_to=b'static/%Y_%m_%d/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
