# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from armery.models import Weapon, Armor, Others, Spell
from heroquest.users.models import User


class Character(models.Model):
    name = models.CharField(max_length=180, verbose_name=_("Nombre"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Descripción"))
    image = models.ImageField(upload_to='character', blank=True, null=True, verbose_name=_("Imágen"))
    p_mind = models.IntegerField(verbose_name=_("Puntos de mente"))
    p_body = models.IntegerField(verbose_name=_("Puntos de cuerpo"))
    attack = models.IntegerField(blank=True, null=True, verbose_name=_("Ataque"))
    defend = models.IntegerField(blank=True, null=True, verbose_name=_("Defensa"))
    move = models.IntegerField(blank=True, null=True, verbose_name=_("Moviemiento"))
    magic = models.BooleanField(default=False, verbose_name=_("Magia"))
    magic_cards = models.IntegerField(blank=True, null=True, verbose_name=_("Cartas de Magia"))
    suit_card = models.IntegerField(blank=True, null=True, verbose_name=_("Palos de Magia"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Personaje')
        verbose_name_plural = _('Personajes')
        ordering = ('name',)


class Adventure(models.Model):
    name = models.CharField(max_length=180, verbose_name=_("Nombre"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Descripción"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Aventura')
        verbose_name_plural = _('Aventuras')
        ordering = ('name',)


class Player(models.Model):
    name = models.CharField(max_length=180, verbose_name=_("Nombre"))
    image = models.ImageField(upload_to='player', blank=True, null=True, verbose_name=_("Imágen"))
    character = models.ForeignKey(Character, verbose_name=_("Personaje"))
    gold_coins = models.IntegerField(blank=True, null=True, verbose_name=_("Monedas de Oro"))
    p_mind = models.IntegerField(verbose_name=_("Puntos de Mente"))
    p_body = models.IntegerField(verbose_name=_("Puntos de Cuerpo"))
    level = models.IntegerField(verbose_name=_("Nivel"))
    weapon = models.ForeignKey(Weapon, blank=True, null=True, related_name='weapons', verbose_name=_("Armas"))
    armor = models.ForeignKey(Armor, blank=True, null=True, related_name='armor', verbose_name=_("Armaduras"))
    others = models.ForeignKey(Others, blank=True, null=True, related_name='others', verbose_name=_("Otros"))
    spell = models.ManyToManyField(Spell, blank=True, null=True, related_name='spells', verbose_name=_("Hechizos"))
    adventures = models.ManyToManyField(Adventure, blank=True, null=True, verbose_name=_("Participo en las Aventuras"),
                                        related_name='adventures')
    user = models.OneToOneField(User, null=True, related_name="user", verbose_name=_("Usuario"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Jugador')
        verbose_name_plural = _('Jugadores')
        ordering = ('name',)


class Monster(models.Model):
    name = models.CharField(max_length=180, verbose_name=_("Nombre"))
    image = models.ImageField(upload_to='monster', blank=True, null=True, verbose_name=_("Imágen"))
    p_mind = models.IntegerField(verbose_name=_("Puntos de mente"))
    p_body = models.IntegerField(verbose_name=_("Puntos de cuerpo"))
    defend = models.IntegerField(blank=True, null=True, verbose_name=_("Defensa"))
    move = models.IntegerField(blank=True, null=True, verbose_name=_("Moviemiento"))
    attack_body2body = models.IntegerField(blank=True, null=True, verbose_name=_("Ataque cuerpo a cuerpo"))
    attack_distance = models.IntegerField(blank=True, null=True, verbose_name=_("Ataque a distancia"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Monstruo')
        verbose_name_plural = _('Monstruos')
        ordering = ('name',)


class TypeRule(models.Model):
    name = models.CharField(max_length=180, verbose_name=_("Nombre"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Descripción"))


class Rules(models.Model):
    name = models.CharField(max_length=180, verbose_name=_("Nombre"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Descripción"))
    image = models.ImageField(upload_to='player', blank=True, null=True, verbose_name=_("Imágen"))
    type_rule = models.ForeignKey(TypeRule, null=True, related_name='armor', verbose_name=_("Tipo"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Regla')
        verbose_name_plural = _('Reglas')
        ordering = ('name',)
