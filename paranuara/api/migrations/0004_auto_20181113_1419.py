# Generated by Django 2.1.3 on 2018-11-13 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181113_1320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companies',
            old_name='name',
            new_name='company',
        ),
    ]
