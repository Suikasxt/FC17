# Generated by Django 3.0.2 on 2020-02-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FC17Website', '0006_auto_20200205_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ai',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
