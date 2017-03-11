# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-08 11:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuesr',
            old_name='username',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='myuesr',
            old_name='userpass',
            new_name='user_pass',
        ),
        migrations.AddField(
            model_name='myuesr',
            name='user_regdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 8, 11, 57, 39, 245006)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuesr',
            name='user_status',
            field=models.IntegerField(default=1),
        ),
    ]
