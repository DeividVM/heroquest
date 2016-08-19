# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'special',)
    search_fields = ('name',)


admin.site.register(Weapon, WeaponAdmin)


class ArmorAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'special',)
    search_fields = ('name',)


admin.site.register(Armor, ArmorAdmin)


class OthersAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'magic_equipment', 'special',)
    search_fields = ('name',)


admin.site.register(Others, OthersAdmin)


class MagigEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost',)
    search_fields = ('name',)


admin.site.register(MagicEquipment, MagigEquipmentAdmin)


class SpellAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type',)
    search_fields = ('name',)


admin.site.register(Spell, SpellAdmin)
