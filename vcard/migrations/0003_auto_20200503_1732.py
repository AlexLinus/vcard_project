# Generated by Django 2.2.4 on 2020-05-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcard', '0002_auto_20200503_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='name',
            field=models.CharField(default='ALEX', max_length=200, verbose_name='Имя на главной'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='nickname',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Никнейм на главной'),
        ),
    ]
