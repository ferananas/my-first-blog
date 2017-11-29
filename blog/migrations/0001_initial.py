# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 07:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=200)),
                ('tekst', models.TextField()),
                ('creatie_datum', models.DateTimeField(default=django.utils.timezone.now)),
                ('publicatie_datum', models.DateTimeField(blank=True, null=True)),
                ('schrijver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
