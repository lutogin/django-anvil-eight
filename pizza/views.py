from django.shortcuts import render
from . import models


def index(req):
    """Индексный контроллер для вывода"""

    """Разобьем ингридиенты по массиву в соответсвии с их группой"""
    elements_lst = []
    elements = {}

    for group in models.Group.objects.all():
        current_ingts = models.Ingredient.objects.filter(group__id=group.id)
        elements[group.name] = current_ingts
        elements[group.name] = {'type': group.type}

    return render(req, 'index.html', context={
        'elements': elements
    })
