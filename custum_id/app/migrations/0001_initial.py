# Generated by Django 3.0.3 on 2020-12-12 10:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custum_ID',
            fields=[
                ('custum_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Custum_ID1',
            fields=[
                ('custum_id1', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
