# Generated by Django 4.2.2 on 2023-06-15 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edwizy_app', '0008_activebot_total_trades_activebot_win_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='activebot',
            name='time_frame',
            field=models.CharField(default=15, max_length=100),
            preserve_default=False,
        ),
    ]
