# Generated by Django 2.2 on 2019-04-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='views_cnt',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
