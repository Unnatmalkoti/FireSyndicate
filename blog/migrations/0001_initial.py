# Generated by Django 2.2.1 on 2019-07-05 12:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('post_type', models.CharField(choices=[('R', 'Recruitment'), ('A', 'Announcment'), ('N', 'News'), ('G', 'Guide'), ('P', 'Pep Talk')], max_length=50, verbose_name='Type')),
                ('body', ckeditor.fields.RichTextField()),
                ('views', models.PositiveIntegerField(verbose_name='Views')),
            ],
        ),
    ]
