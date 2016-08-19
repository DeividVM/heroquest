# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

from heroquest.models import *


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width=350px height=400px /></a> %s ' %
                          (image_url, image_url, file_name, _('Change:')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class ImageWidgetAdmin(admin.ModelAdmin):
    image_fields = []

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.image_fields:
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageWidgetAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class CharacterAdmin(ImageWidgetAdmin):
    list_display = ('name', 'p_mind', 'p_body', 'attack', 'defend', 'move')
    search_fields = ('name',)
    image_fields = ['image', ]


admin.site.register(Character, CharacterAdmin)


class MonsterAdmin(ImageWidgetAdmin):
    list_display = ('name', 'p_mind', 'p_body', 'defend', 'move')
    search_fields = ('name',)
    image_fields = ['image', ]


admin.site.register(Monster, MonsterAdmin)


class AdventureAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Adventure, AdventureAdmin)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'character', 'gold_coins', 'p_mind', 'p_body', 'level', 'weapon', 'armor', 'others',)
    search_fields = ('name',)


admin.site.register(Player, PlayerAdmin)


class RulesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Rules, RulesAdmin)
