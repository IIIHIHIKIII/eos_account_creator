# Generated by Django 2.0.6 on 2018-06-16 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_pricedata'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='coinbase_charge',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='coinbase_code',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='payment_received',
            field=models.BooleanField(default=False),
        ),
    ]
