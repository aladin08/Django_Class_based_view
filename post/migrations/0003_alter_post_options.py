# Generated by Django 4.0.2 on 2022-02-07 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_modelname_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'managed': True, 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
