# Generated by Django 2.2.4 on 2020-09-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0012_auto_20200913_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='order_index',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
    ]
