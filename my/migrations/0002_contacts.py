# Generated by Django 5.0.2 on 2025-02-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
    ]
