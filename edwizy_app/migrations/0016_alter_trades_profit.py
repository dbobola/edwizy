# Generated by Django 4.2.2 on 2023-06-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edwizy_app', '0015_alter_profile_no_of_long_positions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='profit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
