# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-02-21 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fibonacci', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippet',
            new_name='Fibonacci',
        ),
    ]