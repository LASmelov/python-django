# Generated by Django 4.2.2 on 2023-06-19 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_rename_book_develop'),
    ]

    operations = [
        migrations.AddField(
            model_name='develop',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]