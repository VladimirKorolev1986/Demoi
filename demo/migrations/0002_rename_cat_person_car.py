# Generated by Django 4.2.3 on 2023-07-17 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='cat',
            new_name='car',
        ),
    ]