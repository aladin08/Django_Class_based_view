# Generated by Django 4.0.2 on 2022-02-07 10:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=1000)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='post-img/')),
            ],
            options={
                'verbose_name': 'ModelName',
                'verbose_name_plural': 'ModelNames',
                'db_table': '',
                'managed': True,
            },
        ),
    ]