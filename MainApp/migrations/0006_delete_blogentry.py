# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 12:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_submittedtip'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogEntry',
        ),
    ]