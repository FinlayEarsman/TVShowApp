# Generated by Django 3.1.7 on 2021-03-31 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TVShowApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='show',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='show',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
