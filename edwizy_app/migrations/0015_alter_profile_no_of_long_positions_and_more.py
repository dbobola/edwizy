# Generated by Django 4.2.2 on 2023-06-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edwizy_app', '0014_alter_profile_account_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='no_of_long_positions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='no_of_loss_trades',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='no_of_profit_trades',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='no_of_short_positions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='no_of_total_trades',
            field=models.IntegerField(default=0),
        ),
    ]
