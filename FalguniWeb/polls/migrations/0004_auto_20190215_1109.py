# Generated by Django 2.1.7 on 2019-02-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190215_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_nominated',
            field=models.BooleanField(verbose_name=False),
        ),
    ]
