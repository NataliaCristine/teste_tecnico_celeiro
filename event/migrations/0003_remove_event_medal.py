# Generated by Django 4.0.5 on 2022-06-06 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_medal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='medal',
        ),
    ]
