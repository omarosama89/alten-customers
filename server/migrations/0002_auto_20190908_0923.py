# Generated by Django 2.2.5 on 2019-09-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(max_length=100),
        ),
    ]
