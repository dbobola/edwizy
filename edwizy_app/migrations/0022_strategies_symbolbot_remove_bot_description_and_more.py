# Generated by Django 4.2.2 on 2023-06-28 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edwizy_app', '0021_remove_symbol_symbol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strategies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SymbolBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bot',
            name='description',
        ),
        migrations.RemoveField(
            model_name='bot',
            name='name',
        ),
        migrations.AddField(
            model_name='bot',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bot',
            name='order_size',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bot',
            name='order_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bot',
            name='risk_reward',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bot',
            name='time_frame',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bot',
            name='total_trades',
            field=models.CharField(default=0.0, max_length=100),
        ),
        migrations.AddField(
            model_name='bot',
            name='win_rate',
            field=models.CharField(default=0.0, max_length=100),
        ),
        migrations.AddField(
            model_name='symbol',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='edwizy_app.profile'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Activebot',
        ),
        migrations.AddField(
            model_name='symbolbot',
            name='bot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edwizy_app.bot'),
        ),
        migrations.AddField(
            model_name='symbolbot',
            name='symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edwizy_app.symbol'),
        ),
        migrations.AddField(
            model_name='bot',
            name='strategy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='edwizy_app.strategies'),
        ),
    ]
