# Generated by Django 3.1 on 2020-09-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0010_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='pic_folder/booksapp/no-img.jpg', upload_to='pic_folder/booksapp/'),
        ),
    ]