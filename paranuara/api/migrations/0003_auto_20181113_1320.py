# Generated by Django 2.1.3 on 2018-11-13 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181113_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fruits',
            old_name='fruit',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tags',
            old_name='tag',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='vegetables',
            old_name='vegetable',
            new_name='name',
        ),
    ]
