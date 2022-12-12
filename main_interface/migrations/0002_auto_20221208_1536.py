# Generated by Django 3.2.15 on 2022-12-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_interface', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='balance',
            field=models.CharField(default='0', max_length=12),
        ),
        migrations.AddField(
            model_name='userdata',
            name='day_results',
            field=models.CharField(default='0', max_length=12),
        ),
        migrations.AddField(
            model_name='userdata',
            name='results',
            field=models.CharField(default='0', max_length=12),
        ),
        migrations.AddField(
            model_name='userdata',
            name='volume',
            field=models.CharField(default='0', max_length=12),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='previous_trade_id',
            field=models.CharField(default='0', max_length=60),
        ),
    ]