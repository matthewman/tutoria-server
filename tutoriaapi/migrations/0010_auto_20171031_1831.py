# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoriaapi', '0009_auto_20171031_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupiedsession',
            name='userProfileSet',
            field=models.ManyToManyField(related_name='occupiedSessionSet', related_query_name='occupiedSessionSet', to='tutoriaapi.UserProfile'),
        ),
    ]
