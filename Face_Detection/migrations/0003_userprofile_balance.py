# Generated by Django 3.0 on 2021-01-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Face_Detection', '0002_auto_20210104_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='balance',
            field=models.IntegerField(default=1000),
        ),
    ]
