# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-29 08:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighborhood', '0003_auto_20191024_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('Author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('author_profile', models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='neighborhood.Profile')),
                ('neighborhood', models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='neighborhood.Neighborhood')),
            ],
            options={
                'verbose_name': 'My Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-pub_date'],
            },
        ),
    ]
