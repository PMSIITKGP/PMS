# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-06 04:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_job_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edit_details',
            old_name='c_perm',
            new_name='register',
        ),
        migrations.RenameField(
            model_name='job_desc',
            old_name='c_name',
            new_name='register',
        ),
    ]