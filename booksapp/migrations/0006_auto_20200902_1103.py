# Generated by Django 3.1 on 2020-09-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0005_auto_20200902_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='number',
            field=models.IntegerField(),
        ),
    ]
