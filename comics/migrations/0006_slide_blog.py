# Generated by Django 2.2.1 on 2019-08-01 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190721_2138'),
        ('comics', '0005_auto_20190731_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='Blog Post'),
        ),
    ]
