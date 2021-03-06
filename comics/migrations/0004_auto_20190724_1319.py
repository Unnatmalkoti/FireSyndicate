# Generated by Django 2.2.1 on 2019-07-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0003_auto_20190724_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='default_display_style',
            field=models.CharField(choices=[('M', 'Manga Style'), ('W', 'Webtoon Style')], max_length=1),
        ),
        migrations.AlterField(
            model_name='comic',
            name='status',
            field=models.CharField(choices=[('W', 'Working'), ('H', 'On Hold'), ('D', 'Dropped'), ('I', 'Inactive')], max_length=1),
        ),
    ]
