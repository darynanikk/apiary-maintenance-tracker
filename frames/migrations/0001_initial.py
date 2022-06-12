# Generated by Django 4.0.4 on 2022-06-12 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hives', '0003_auto_20220612_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('status', models.CharField(default='test', max_length=55)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('moveHistory', models.CharField(max_length=255)),
                ('hive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frames', to='hives.hive')),
            ],
        ),
    ]
