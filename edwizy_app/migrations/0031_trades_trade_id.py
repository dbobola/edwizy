# Generated by Django 4.2.2 on 2023-07-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edwizy_app', '0030_trades_bot'),
    ]

    operations = [
        migrations.AddField(
            model_name='trades',
            name='trade_id',
            field=models.CharField(default=0, max_length=100),
        ),
    ]