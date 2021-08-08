# Generated by Django 3.2.5 on 2021-08-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0007_auto_20210729_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='seeking_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='seeking_talent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='venue',
            name='website_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]