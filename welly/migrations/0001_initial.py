# Generated by Django 5.0 on 2024-03-30 22:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('specialist_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkList',
            fields=[
                ('work_list_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_id', models.CharField(max_length=20)),
                ('patient_name', models.CharField(max_length=100)),
                ('encounter_date', models.DateField()),
                ('assignment_date', models.DateField()),
                ('open_queries', models.IntegerField()),
                ('sys_priority', models.IntegerField()),
                ('manual_priority', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('physician', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('facility', models.CharField(max_length=100)),
                ('assigned_specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='welly.specialist')),
            ],
        ),
    ]