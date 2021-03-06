# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('position', models.IntegerField(default=0)),
                ('thumnails', models.URLField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='category.Category')),
            ],
        ),
    ]
