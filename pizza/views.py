from django.shortcuts import render
from . import models


def index(req):
    """Индексный контроллер для вывода"""

    """Разобьем ингридиенты по массиву в соответсвии с их группой"""
    elements = dict()

    for group in models.Group.objects.all():
        elements[group.id] = {'group': group}
        elements[group.id].update({'ingredients': {}})
        for ing in models.Ingredient.objects.filter(group_id=group.id):
            elements[group.id]['ingredients'].update({ing.id: ing})

    return render(req, 'index.html', context={
        'elements': elements
    })
