# Generated by Django 2.2.4 on 2020-05-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0003_auto_20200503_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='specialization',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Позиция (специализация)'),
        ),
    ]