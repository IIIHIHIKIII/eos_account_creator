# Generated by Django 2.0.6 on 2018-06-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0012_purchase_coinbase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='active_key',
            field=models.CharField(default='', max_length=53),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='owner_key',
            field=models.CharField(default='', max_length=53),
            preserve_default=False,
        ),
    ]