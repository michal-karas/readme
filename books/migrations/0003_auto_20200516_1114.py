# Generated by Django 3.0.5 on 2020-05-16 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
