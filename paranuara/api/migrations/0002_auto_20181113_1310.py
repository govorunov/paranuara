# Generated by Django 2.1.3 on 2018-11-13 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vegetables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vegetable', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='people',
            name='favourite_food',
        ),
        migrations.RemoveField(
            model_name='people',
            name='favourite_fruit',
        ),
        migrations.RemoveField(
            model_name='people',
            name='favourite_vegetable',
        ),
        migrations.AlterField(
            model_name='companies',
            name='index',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='address',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='balance',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='api.Companies'),
        ),
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='gender',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='greeting',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='guid',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='has_died',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='index',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='phone',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='picture',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='registered',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='people',
            name='tags',
        ),
        migrations.AddField(
            model_name='people',
            name='favourite_fruits',
            field=models.ManyToManyField(blank=True, related_name='people', to='api.Fruits'),
        ),
        migrations.AddField(
            model_name='people',
            name='favourite_vegetables',
            field=models.ManyToManyField(blank=True, related_name='people', to='api.Vegetables'),
        ),
        migrations.AddField(
            model_name='people',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='people', to='api.Tags'),
        ),
    ]
