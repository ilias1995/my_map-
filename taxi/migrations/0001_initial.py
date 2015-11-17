# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registr_taxi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('second_name', models.CharField(max_length=200, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('phone_number', models.CharField(max_length=b'200', verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0')),
                ('car_model', models.CharField(max_length=200, verbose_name=b'\xd0\x9c\xd0\xbe\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c \xd0\xbc\xd0\xb0\xd1\x88\xd0\xb8\xd0\xbd\xd1\x8b')),
                ('car_photo', models.FileField(upload_to=b'cars_photo', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe \xd0\xbc\xd0\xb0\xd1\x88\xd0\xb8\xd0\xbd\xd1\x8b')),
                ('price', models.IntegerField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0')),
                ('from_where', models.CharField(max_length=200, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xba\xd1\x83\xd0\xb4\xd0\xb0')),
                ('where', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd1\x83\xd0\xb4\xd0\xb0')),
                ('end_time', models.DateField(verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbe\xd0\xba\xd0\xb0\xd0\xbd\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0')),
                ('about', models.TextField(verbose_name=b'\xd0\x95\xd1\x89\xd0\xb5 \xd0\xb8\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f')),
                ('add_time', models.DateField(auto_now=True)),
            ],
        ),
    ]
