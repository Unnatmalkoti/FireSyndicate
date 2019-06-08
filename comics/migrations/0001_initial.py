# Generated by Django 2.2 on 2019-04-29 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('views_cnt', models.PositiveIntegerField(default=0)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('artist', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('cover', models.ImageField(upload_to='')),
                ('status', models.PositiveSmallIntegerField(default=True)),
                ('views_cnt', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('page_number', models.PositiveIntegerField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comics.Chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='comic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comics.Comic'),
        ),
    ]
