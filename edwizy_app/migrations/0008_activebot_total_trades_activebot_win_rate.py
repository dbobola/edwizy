# Generated by Django 4.2.2 on 2023-06-15 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edwizy_app', '0007_alter_trades_status_activebot'),
    ]

    operations = [
        migrations.AddField(
            model_name='activebot',
            name='total_trades',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activebot',
            name='win_rate',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
