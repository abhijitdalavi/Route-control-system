# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-24 20:04

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nit', models.IntegerField(primary_key=True, serialize=False)),
                ('razon_social', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo_media')),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('ciudad', models.CharField(default='', max_length=50)),
                ('direccion', models.TextField()),
                ('activo_inactivo', models.BooleanField(default=True)),
            ],
        ),
    ]