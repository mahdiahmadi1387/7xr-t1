# Generated by Django 3.1 on 2020-09-27 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0009_auto_20200914_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
