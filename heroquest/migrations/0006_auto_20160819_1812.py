# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-19 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroquest', '0005_auto_20160819_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='spell',
            field=models.ManyToManyField(blank=True, null=True, related_name='spells', to='armery.Spell', verbose_name='Hechizos'),
        ),
    ]