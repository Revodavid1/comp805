# Generated by Django 2.0.2 on 2018-02-19 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20180211_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=40)),
                ('Last_name', models.CharField(max_length=40)),
            ],
        ),
    ]
