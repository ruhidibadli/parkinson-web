# Generated by Django 4.1.4 on 2022-12-25 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkinsonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppe', models.FloatField(default=0)),
                ('shimmerapq5', models.FloatField(default=0)),
                ('mdvpfo', models.FloatField(default=0)),
                ('mdvpshimmer', models.FloatField(default=0)),
                ('mdvpfhi', models.FloatField(default=0)),
                ('mdvpflo', models.FloatField(default=0)),
                ('rpde', models.FloatField(default=0)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
