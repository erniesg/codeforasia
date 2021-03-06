# Generated by Django 3.0.4 on 2020-03-06 06:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200306_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('item_1', models.CharField(max_length=100)),
                ('cost_1', models.IntegerField()),
                ('item_2', models.CharField(max_length=100)),
                ('cost_2', models.IntegerField()),
                ('item_3', models.CharField(max_length=100)),
                ('cost_3', models.IntegerField()),
                ('item_4', models.CharField(max_length=100)),
                ('cost_4', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='form',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 14, 1, 10, 908973), verbose_name='published date'),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 14, 1, 10, 909971), verbose_name='Birth data'),
        ),
        migrations.AlterField(
            model_name='site',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 14, 1, 10, 907975), verbose_name='published date'),
        ),
    ]
