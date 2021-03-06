# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-19 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armery', '0003_armor_others'),
    ]

    operations = [
        migrations.CreateModel(
            name='MagicEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='magig', verbose_name='Imágen')),
                ('cost', models.IntegerField(verbose_name='Costo')),
            ],
            options={
                'verbose_name_plural': 'Equipos Magicos',
                'verbose_name': 'Equipo Magico',
                'ordering': ('name',),
            },
        ),
        migrations.RemoveField(
            model_name='armor',
            name='magic_equipment',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='magic_equipment',
        ),
        migrations.AlterField(
            model_name='armor',
            name='special',
            field=models.BooleanField(default=False, verbose_name='Especial'),
        ),
        migrations.AlterField(
            model_name='others',
            name='special',
            field=models.BooleanField(default=False, verbose_name='Especial'),
        ),
    ]
