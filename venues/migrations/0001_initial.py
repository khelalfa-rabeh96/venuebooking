# Generated by Django 3.2.5 on 2021-07-27 11:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('phone', models.CharField(blank=True, max_length=120, null=True)),
                ('image_link', models.CharField(blank=True, max_length=120, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=120, null=True)),
                ('genre', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), size=None)),
            ],
        ),
    ]
