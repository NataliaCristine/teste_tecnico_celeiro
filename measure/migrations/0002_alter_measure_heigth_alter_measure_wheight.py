# Generated by Django 4.0.5 on 2022-06-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure',
            name='heigth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='measure',
            name='wheight',
            field=models.IntegerField(null=True),
        ),
    ]
