# Generated by Django 3.2.5 on 2021-08-07 10:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_alter_show_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
