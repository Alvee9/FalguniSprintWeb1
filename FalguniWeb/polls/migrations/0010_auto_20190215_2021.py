# Generated by Django 2.1.7 on 2019-02-15 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20190215_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='vote_casted_PM',
            new_name='vote_casted',
        ),
        migrations.RemoveField(
            model_name='user',
            name='vote_casted_councillor',
        ),
        migrations.RemoveField(
            model_name='user',
            name='vote_casted_mayor',
        ),
    ]
