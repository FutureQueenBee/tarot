# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-22 02:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='minorarcana',
            name='number',
        ),
        migrations.AddField(
            model_name='minorarcana',
            name='rank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learn.Rank'),
            preserve_default=False,
        ),
    ]