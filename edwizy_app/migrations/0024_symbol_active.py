# Generated by Django 4.2.2 on 2023-06-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edwizy_app', '0023_remove_symbol_broker'),
    ]

    operations = [
        migrations.AddField(
            model_name='symbol',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
