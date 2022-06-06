# Generated by Django 4.0.5 on 2022-06-05 17:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('heigth', models.IntegerField()),
                ('wheight', models.IntegerField()),
                ('age', models.CharField(max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='user.user')),
            ],
        ),
    ]
