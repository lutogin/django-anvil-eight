from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from .models import Group, Ingredient
from .forms.forms import BuyForm
from .mailing.mailing import send_mail
import re
import json


def index(req):
    """Индексный контроллер для вывода"""

    """Разобьем ингридиенты по массиву в соответсвии с их группой"""
    elements = {}
    elements_list = []

    for group in Group.objects.all():
        elements[group.id] = {'group': group}
        elements[group.id].update({'ingredients': {}})
        for ing in group.ingredients.all():
            elements[group.id]['ingredients'].update({ing.id: ing})

    return render(req, 'index.html', context={
        'elements': elements
    })


def submit_order(req):
    """Форма подтверждения заказа"""

    if req.method == 'GET':
        return HttpResponsePermanentRedirect('/')

    not_price_ingredients = []
    for not_price_ing in Group.objects.filter(type='radio'):
        not_price_ingredients.append(not_price_ing.name)

    data_post = req.POST
    summaty_price = 0
    data_bill = []

    for item in data_post:

        # if item in not_price_ingredients:
        #     """Добавим в обект с заказом поля без цен(в случае выбора теста)"""
        #     data_bill.append({'name': item, 'count': Ingredient.objects.get(id=data_post[item]).name})
        #     continue

        if re.match(r'^id-item-free-[0-9]*$', item):
            """С даннми приходят служебная информация, выхватим нужные значения"""
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


        # if data_post[item].isdigit() and int(data_post[item]) != 0:


    form = BuyForm(initial={'summary_price': summaty_price})
    return render(req, 'submit-order.html', context={
        'form': form,
        'data_bill': data_bill,
        'data_bill_json': json.dumps(data_bill)
    })


def submit_order_finish(req):
    """Отправка заказа"""

    if req.method == 'POST':
        customer_name = req.POST['name']
        content = ''

        for item in json.loads(req.POST['data_bill_json']):
            content += '<li>'+item['name']+': '+item['count']+'</li>'

        body = '<p>Здратсвуйте, '+customer_name+'.</p><p>Ваш заказ принят в обработку</p><ul>'+content+'</ul><p><b>Общая стоимость: '+req.POST['summary_price']+'$</b></p>'
        send_mail(req.POST['email'], body)

        return render(req, 'done.html', context={'name': customer_name})
