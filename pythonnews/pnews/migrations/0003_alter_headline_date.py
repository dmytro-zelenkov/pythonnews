# Generated by Django 4.0.5 on 2022-06-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnews', '0002_headline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='date',
            field=models.CharField(max_length=64),
        ),
    ]
