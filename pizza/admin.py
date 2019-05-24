from django.contrib import admin
from . import models


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'sort_index')
    fields = ['name', 'type', 'sort_index']


@admin.register(models.Ingredient)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'price')
    fields = ['name', 'price', 'group']
