# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-02-06 21:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0005_auto_20190206_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='email_address',
        ),
    ]