# Generated by Django 3.2.13 on 2022-06-12 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiaries', '0006_alter_apiary_location_alter_apiary_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiary',
            name='location',
            field=models.JSONField(default=dict),
        ),
    ]
