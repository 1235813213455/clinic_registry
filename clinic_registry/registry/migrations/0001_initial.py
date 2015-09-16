# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('time', models.IntegerField(default=9)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('second_name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='doctor',
            field=models.ForeignKey(to='registry.Doctor'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='patient',
            field=models.ForeignKey(to='registry.Patient'),
        ),
    ]
