# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoriaapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OccupiedSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ManyToManyField(related_name='occupiedSessions', related_query_name='occupiedSessions', to='tutoriaapi.UserProfile')),
            ],
        ),
    ]