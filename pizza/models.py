from django.db import models


class Group(models.Model):
    """Модель группы для ингридиентов"""
    INPUT_CHOISES = (
        ('radio', 'Радио-кнопки'),
        ('input', 'Ввод'),
        ('checkbox', 'Флажки'),
        ('select', 'Выпадающий список'),
    )

    name = models.CharField(max_length=64, help_text='Название группы ингредиентов')
    type = models.CharField(max_length=7, choices=INPUT_CHOISES, default='input', help_text='Поля выбора')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель ингридиента"""
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, help_text='Название ингредиента')
    price = models.FloatField(null=True, default=0, help_text='Цена за еденицу')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

