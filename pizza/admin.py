from django.contrib import admin
from . import models


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    fields = ['name', 'type']


@admin.register(models.Ingredient)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'price')
    fields = ['name', 'price', 'group']
