# Generated by Django 3.2.5 on 2021-07-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0005_alter_venue_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='image_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]