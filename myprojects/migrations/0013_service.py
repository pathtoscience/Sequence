# Generated by Django 3.2.8 on 2022-03-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0012_auto_20210618_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
