# Generated by Django 2.2.1 on 2019-05-23 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0006_auto_20190523_2354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name']},
        ),
    ]