# Generated by Django 3.1.2 on 2020-11-06 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myModels', '0004_song'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='user',
            new_name='singers',
        ),
    ]