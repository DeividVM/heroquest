# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-18 19:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('armery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Aventuras',
                'verbose_name': 'Aventura',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='character', verbose_name='Imágen')),
                ('p_mind', models.IntegerField(verbose_name='Puntos de mente')),
                ('p_body', models.IntegerField(verbose_name='Puntos de cuerpo')),
                ('attack', models.IntegerField(blank=True, null=True, verbose_name='Ataque')),
                ('defend', models.IntegerField(blank=True, null=True, verbose_name='Defensa')),
                ('move', models.IntegerField(blank=True, null=True, verbose_name='Moviemiento')),
                ('magic', models.BooleanField(default=False, verbose_name='Magia')),
                ('magic_cards', models.IntegerField(blank=True, null=True, verbose_name='Cartas de Magia')),
                ('suit_card', models.IntegerField(blank=True, null=True, verbose_name='Palos de Magia')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Personajes',
                'verbose_name': 'Personaje',
            },
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Nombre')),
                ('image', models.ImageField(blank=True, null=True, upload_to='monster', verbose_name='Imágen')),
                ('p_mind', models.IntegerField(verbose_name='Puntos de mente')),
                ('p_body', models.IntegerField(verbose_name='Puntos de cuerpo')),
                ('defend', models.IntegerField(blank=True, null=True, verbose_name='Defensa')),
                ('move', models.IntegerField(blank=True, null=True, verbose_name='Moviemiento')),
                ('attack_body2body', models.IntegerField(blank=True, null=True, verbose_name='Ataque cuerpo a cuerpo')),
                ('attack_distance', models.IntegerField(blank=True, null=True, verbose_name='Ataque a distancia')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Monstruos',
                'verbose_name': 'Monstruo',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Nombre')),
                ('image', models.ImageField(blank=True, null=True, upload_to='player', verbose_name='Imágen')),
                ('gold_coins', models.IntegerField(blank=True, null=True, verbose_name='Monedas de Oro')),
                ('p_mind', models.IntegerField(verbose_name='Puntos de Mente')),
                ('p_body', models.IntegerField(verbose_name='Puntos de Cuerpo')),
                ('level', models.IntegerField(verbose_name='Nivel')),
                ('adventures', models.ManyToManyField(related_name='adventures', to='heroquest.Adventure', verbose_name='Participo en las Aventuras')),
                ('armor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='armor', to='armery.Armor', verbose_name='Armaduras')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heroquest.Character', verbose_name='Personaje')),
                ('spell', models.ManyToManyField(null=True, related_name='spells', to='armery.Spell', verbose_name='Hechizos')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('weapon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weapons', to='armery.Weapon', verbose_name='Armas')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Jugadores',
                'verbose_name': 'Jugador',
            },
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='player', verbose_name='Imágen')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Reglas',
                'verbose_name': 'Regla',
            },
        ),
        migrations.CreateModel(
            name='TypeRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.AddField(
            model_name='rules',
            name='type_rule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='armor', to='heroquest.TypeRule', verbose_name='Tipo'),
        ),
    ]
