# Generated by Django 2.1.3 on 2018-11-13 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181113_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='eye_color',
            new_name='eyeColor',
        ),
    ]
