# Generated by Django 2.2.4 on 2020-09-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0010_siteconfig_is_services_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='is_portfolio_active',
            field=models.BooleanField(default=True, verbose_name='Включить портфолио'),
        ),
    ]
