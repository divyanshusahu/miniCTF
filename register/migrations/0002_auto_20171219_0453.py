# Generated by Django 2.0 on 2017-12-19 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='username',
            new_name='teamname',
        ),
    ]
