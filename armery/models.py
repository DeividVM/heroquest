# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Weapon(models.Model):
    name = models.CharField(max_length=180, verbose_name=_("Nombre"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Descripción"))
    image = models.ImageField(upload_to='weapon', blank=True, null=True, verbose_name=_("Imágen"))
    cost = models.IntegerField(verbose_name=_("Costo"))
    special = models.BooleanField(default=False, verbose_name=_("Arma Especial"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Arma')
        verbose_name_plural = _('Armas')
        ordering = ('name',)


class Armor(models.Model):
    name = models.CharField(max_length=180, verbose_name=_("Nombre"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Descripción"))
    image = models.ImageField(upload_to='weapon', blank=True, null=True, verbose_name=_("Imágen"))
    cost = models.IntegerField(verbose_name=_("Costo"))
    special = models.BooleanField(default=False, verbose_name=_("Especial"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Armadura')
        verbose_name_plural = _('Armaduras')
        ordering = ('name',)


class MagicEquipment(models.Model):
    name = models.CharField(max_length=180, verbose_name=_("Nombre"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Descripción"))
    image = models.ImageField(upload_to='magig', blank=True, null=True, verbose_name=_("Imágen"))
    cost = models.IntegerField(verbose_name=_("Costo"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Equipo Magico')
        verbose_name_plural = _('Equipos Magicos')
        ordering = ('name',)


class Others(models.Model):
    name = models.CharField(max_length=180, verbose_name=_("Nombre"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Descripción"))
    image = models.ImageField(upload_to='weapon', blank=True, null=True, verbose_name=_("Imágen"))
    cost = models.IntegerField(verbose_name=_("Costo"))
    magic_equipment = models.BooleanField(default=False, verbose_name=_("Equipo Magico"))
    special = models.BooleanField(default=False, verbose_name=_("Especial"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Otro')
        verbose_name_plural = _('Otros')
        ordering = ('name',)


class Spell(models.Model):
    WATER = 1
    FIRE = 2
    AIR = 3
    SOIL = 4
    TYPE_SPELL_CHOICES = (
        (WATER, _('Agua')),
        (FIRE, _('Fuego')),
        (AIR, _('Aire')),
        (SOIL, _('Tierra')),
    )
    name = models.CharField(max_length=180, verbose_name=_("Nombre"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Descripción"))
    image = models.ImageField(upload_to='weapon', blank=True, null=True, verbose_name=_("Imágen"))
    type = models.IntegerField(choices=TYPE_SPELL_CHOICES, verbose_name=_("Tipo de Magia"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Hechizo')
        verbose_name_plural = _('Hechizos')
        ordering = ('name',)
