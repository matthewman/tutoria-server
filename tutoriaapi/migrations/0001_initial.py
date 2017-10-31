# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 07:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StudentRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentRole', related_query_name='studentRole', to='tutoriaapi.Role')),
            ],
        ),
        migrations.CreateModel(
            name='TutorRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tutorRole', related_query_name='tutorRole', to='tutoriaapi.Role')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=8)),
                ('avatar', models.TextField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userProfile', related_query_name='userProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', related_query_name='roles', to='tutoriaapi.UserProfile'),
        ),
    ]
