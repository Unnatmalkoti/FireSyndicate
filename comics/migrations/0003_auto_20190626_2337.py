# Generated by Django 2.2.1 on 2019-06-26 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0002_auto_20190621_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='tags',
            field=models.ManyToManyField(to='comics.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.URLField(verbose_name='Hyperlink')),
                ('comic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comics.Comic')),
            ],
        ),
    ]