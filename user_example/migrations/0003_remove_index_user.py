# Generated by Django 2.2.4 on 2019-09-03 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_example', '0002_auto_20190903_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='user',
        ),
    ]
