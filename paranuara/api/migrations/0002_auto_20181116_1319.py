# Generated by Django 2.1.3 on 2018-11-16 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='index',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='people',
            name='index',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
