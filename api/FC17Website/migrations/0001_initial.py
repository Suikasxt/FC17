# Generated by Django 3.0.2 on 2020-02-04 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=31)),
                ('introduction', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('information', models.CharField(default='', max_length=1023)),
                ('isCaptain', models.BooleanField(default=False)),
                ('isMember', models.BooleanField(default=False)),
                ('avatar', models.FileField(default='/avatars/default.png', upload_to='avatars/')),
                ('adminLevel', models.IntegerField(default=0)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='belong_to', to='FC17Website.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('content', models.CharField(default='', max_length=4095)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='FC17Website.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=4095)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FC17Website.Notice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FC17Website.User')),
            ],
        ),
    ]
