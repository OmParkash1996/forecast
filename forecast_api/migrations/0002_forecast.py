# Generated by Django 3.2.13 on 2022-04-20 12:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forecast_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forecast', models.JSONField(blank=True, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_emailed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'forecast',
                'managed': True,
            },
        ),
    ]
