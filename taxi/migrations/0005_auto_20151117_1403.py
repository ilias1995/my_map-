# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0004_auto_20151117_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='From_where',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_where', models.CharField(max_length=200, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xba\xd1\x83\xd0\xb4\xd0\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Where',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('where', models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd1\x83\xd0\xb4\xd0\xb0')),
            ],
        ),
        migrations.AlterField(
            model_name='registr_taxi',
            name='from_where',
            field=models.ForeignKey(to='taxi.From_where'),
        ),
        migrations.AlterField(
            model_name='registr_taxi',
            name='where',
            field=models.ForeignKey(to='taxi.Where'),
        ),
    ]
