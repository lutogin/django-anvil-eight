from django.test import TestCase
from ..models import Group, Ingredient


class ModelsTests(TestCase):

    def test_model_group(self):
        """Тест для модели групп"""
        name = 'TestGrup'
        type_input = 'number'
        sort_index = 2

        group = Group.objects.create(name=name, type=type_input, sort_index=sort_index)

        self.assertEqual(group.name, name)
        self.assertEqual(group.type, type_input)
        self.assertEqual(group.sort_index, sort_index)

    def test_model_ingredient(self):
        """Тест для модели ингридиентов"""
        group = Group.objects.create(name='TestGrup', type='number', sort_index=2)
        name = 'TestIngredient'
        price = 1

        ingredient = Ingredient.objects.create(group=group, name=name, price=price)

        self.assertEqual(ingredient.group, group)
        self.assertEqual(ingredient.name, name)
        self.assertEqual(ingredient.price, price)
