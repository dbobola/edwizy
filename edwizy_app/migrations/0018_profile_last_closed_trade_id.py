# Generated by Django 4.2.2 on 2023-06-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edwizy_app', '0017_alter_trades_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_closed_trade_id',
            field=models.IntegerField(default=0),
        ),
    ]
