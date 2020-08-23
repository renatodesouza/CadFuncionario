# Generated by Django 2.2 on 2020-08-22 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200822_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obra',
            name='end',
        ),
        migrations.AddField(
            model_name='obra',
            name='bairro',
            field=models.CharField(default='teste', max_length=255, verbose_name='Bairro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obra',
            name='cidade',
            field=models.CharField(default='sao', max_length=255, verbose_name='Cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obra',
            name='numero',
            field=models.IntegerField(default=1, verbose_name='Numero'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='obra',
            name='rua',
            field=models.CharField(default='dois', max_length=255, verbose_name='Rua'),
            preserve_default=False,
        ),
    ]
