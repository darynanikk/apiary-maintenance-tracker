# Generated by Django 4.0.4 on 2022-06-03 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiaries', '0004_alter_apiary_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apiary',
            old_name='isHidden',
            new_name='is_hidden',
        ),
    ]
