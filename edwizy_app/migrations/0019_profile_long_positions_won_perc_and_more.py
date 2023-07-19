# Generated by Django 4.2.2 on 2023-06-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edwizy_app', '0018_profile_last_closed_trade_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='long_positions_won_perc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='short_positions_won_perc',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='long_positions_won',
            field=models.IntegerField(default=0),
        ),
    ]