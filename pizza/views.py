from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect, HttpResponse
from pizza.models import Group, Ingredient
from pizza.forms.forms import BuyForm
from pizza.utility.mailing import send_mail
import re
import json


def index(req):
    """Индексный контроллер"""

    """Разобьем данные по массиву"""
    elements_lst = []
    elements = {}

    for group in Group.objects.all():
        elements["group"] = group
        elements["ingredients"] = {}
        for ing in group.ingredients.all():
            elements["ingredients"][ing.id] = ing

        elements_lst.append(elements.copy())
        elements.clear()
    return render(req, 'index.html', context={
        'elements': elements_lst
    })


def submit_order(req):
    """Форма подтверждения заказа"""

    if req.method == 'GET':
        return HttpResponsePermanentRedirect('/')

    data_post = req.POST
    summaty_price = 0
    data_bill = []

    for item in data_post:

        if re.match(r'^id-item-free-[0-9]*$', item):
            """С данными с формы приходит служебная информация, выберем только необходимые значения"""
            current_ing = Ingredient.objects.get(id=data_post[item])
            data_bill.append({
                'name': current_ing.group.name,
                'count': current_ing.name
            })
            continue

        if re.match(r'^id-item-[0-9]*$', item) and int(data_post[item]) != 0:
            """Подсчитаем сумму выбраных ингредиентов"""
            current_ing = Ingredient.objects.get(id=re.search(r'\d+', item)[0])
            summaty_price += current_ing.price * int(data_post[item])
            """Сформируем новый словарь содержащий только ифномацию о заказа"""
            data_bill.append({'name': current_ing.name, 'count': data_post[item]})

    form = BuyForm(initial={'summary_price': summaty_price})

    return render(req, 'submit-order.html', context={
        'form': form,
        'data_bill': data_bill,
        'data_bill_json': json.dumps(data_bill)
    })


def submit_order_finish(req):
    """Отправка заказа"""

    if req.method == 'GET':
        return HttpResponsePermanentRedirect('/')

    submit_form = BuyForm(req.POST)
    if submit_form.is_valid():
        customer_name = submit_form.cleaned_data['name']
        content = ''

        for item in json.loads(req.POST['data_bill_json']):
            content += '<li>' + item['name'] + ': ' + item['count'] + '</li>'

        body = '<p>Здратсвуйте, ' + customer_name + '.</p><p>Ваш заказ принят в обработку</p><ul>' + content + \
               '</ul><p><b>Общая стоимость: ' + \
               submit_form.cleaned_data['summary_price'] + '$</b></p>'

        send_mail(submit_form.cleaned_data['email'], body)

        return render(req, 'done.html', context={'name': customer_name})

    """В случае неверно заполненой формы"""
    return HttpResponse("Неверно заполнена форма. Все поля являются обезательными")
