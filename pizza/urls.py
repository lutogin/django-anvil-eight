from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'submit/$', views.submit_order, name='submit_order'),
    re_path(r'finish/$', views.submit_order_finish, name='submit_order_finish')
]
