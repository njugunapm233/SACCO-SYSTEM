# Generated by Django 2.2.5 on 2019-11-30 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191128_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='occupation',
        ),
        migrations.AddField(
            model_name='profile',
            name='Amount',
            field=models.IntegerField(default=0),
        ),
    ]
