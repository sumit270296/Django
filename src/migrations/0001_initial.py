# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 06:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('published_at', models.DateTimeField(default=datetime.datetime(2016, 10, 1, 6, 13, 39, 915881, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('published_at', models.DateTimeField()),
                ('description', models.TextField()),
                ('author_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.Post'),
        ),
    ]
