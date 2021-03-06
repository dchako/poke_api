# Generated by Django 3.2.7 on 2021-09-18 05:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expansion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expansion', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('hp', models.PositiveIntegerField(default=0)),
                ('start_date', models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 18, 2, 25, 52, 40666))),
                ('rarity', models.CharField(choices=[('COMUN', 'comun'), ('NO COMUN', 'no comun'), ('RARA', 'rara')], default='COMUN', max_length=10)),
                ('price', models.FloatField(default=0.0, max_length=99999.9)),
                ('image_cards', models.URLField(blank=True)),
                ('is_firts_edition', models.BooleanField(default=False)),
                ('expansion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expansions', to='pokecards.expansion')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokecards.types')),
            ],
        ),
    ]
