# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0008_registr_taxi_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='user',
        ),
        migrations.AlterField(
            model_name='registr_taxi',
            name='car_model',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9c\xd0\xbe\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c \xd0\xbc\xd0\xb0\xd1\x88\xd0\xb8\xd0\xbd\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='registr_taxi',
            name='car_number',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xbc\xd0\xb0\xd1\x88\xd0\xb8\xd0\xbd\xd1\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='registr_taxi',
            name='from_where',
            field=models.ForeignKey(verbose_name=b'\xd0\x9e\xd1\x82 \xd0\xba\xd1\x83\xd0\xb4\xd0\xb0', to='taxi.From_where'),
        ),
        migrations.AlterField(
            model_name='registr_taxi',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='registr_taxi',
            name='phone_number',
            field=models.CharField(max_length=b'200', verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='registr_taxi',
            name='second_name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='registr_taxi',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='registr_taxi',
            name='where',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd1\x83\xd0\xb4\xd0\xb0', to='taxi.Where'),
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
