# Generated by Django 2.2.1 on 2019-07-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0002_auto_20190704_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='default_display_style',
            field=models.CharField(choices=[('Manga Style', 'M'), ('Webtoon Style', 'W')], default='W', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comic',
            name='status',
            field=models.CharField(choices=[('Working', 'W'), ('On Hold', 'H'), ('Dropped', 'D'), ('Inactive', 'I')], max_length=1),
        ),
    ]
