# Generated by Django 4.2.2 on 2023-06-28 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edwizy_app', '0022_strategies_symbolbot_remove_bot_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symbol',
            name='broker',
        ),
    ]
