# Generated by Django 4.0.5 on 2022-06-13 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pnews', '0004_headline_replies_headline_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headline',
            name='url',
        ),
    ]
