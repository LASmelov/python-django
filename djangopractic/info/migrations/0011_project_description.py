# Generated by Django 4.2.2 on 2023-06-20 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_card_description_alter_developer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание проекта'),
            preserve_default=False,
        ),
    ]
