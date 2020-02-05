# Generated by Django 3.0.2 on 2020-02-05 02:54

import FC17Website.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FC17Website', '0004_auto_20200204_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='AI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('userid', models.IntegerField(default=-1)),
                ('teamname', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('file', models.FileField(upload_to=FC17Website.models.user_dirpath)),
                ('path', models.CharField(max_length=500)),
                ('origin_name', models.CharField(default=models.CharField(max_length=255), max_length=255)),
                ('exact_name', models.CharField(default=models.CharField(default=models.CharField(max_length=255), max_length=255), max_length=255)),
                ('timestamp', models.DateTimeField()),
                ('selected', models.BooleanField(default=False)),
                ('rank_daily', models.IntegerField(default=0)),
                ('rank_overall', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'FileInfo',
                'ordering': ['-timestamp'],
            },
        ),
    ]
