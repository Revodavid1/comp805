# Generated by Django 2.0.2 on 2018-02-19 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='parent_resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
        migrations.AddField(
            model_name='experience',
            name='parent_resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
    ]
