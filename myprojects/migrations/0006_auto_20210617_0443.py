# Generated by Django 2.2 on 2021-06-17 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0005_auto_20210617_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='static/img'),
        ),
    ]