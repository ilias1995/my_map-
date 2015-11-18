# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_registr_taxi_car_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registr_taxi',
            name='car_photo',
            field=models.FileField(default=True, upload_to=b'cars_photo', verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x82\xd0\xbe \xd0\xbc\xd0\xb0\xd1\x88\xd0\xb8\xd0\xbd\xd1\x8b'),
        ),
    ]
