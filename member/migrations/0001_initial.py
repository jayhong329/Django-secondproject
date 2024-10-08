# Generated by Django 5.0.7 on 2024-08-08 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=20, unique=True)),
                ('member_password', models.CharField(max_length=128)),
                ('member_birth', models.DateField()),
                ('member_email', models.EmailField(default='', max_length=200, unique=True)),
                ('member_avatar', models.CharField(default='empty.png', max_length=100)),
                ('last_update', models.DateTimeField(default=datetime.datetime(2024, 8, 8, 19, 56, 53, 465343))),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]
