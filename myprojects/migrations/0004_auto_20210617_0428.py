# Generated by Django 2.2 on 2021-06-17 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0003_auto_20210612_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='static/img'),
        ),
    ]
