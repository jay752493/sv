# Generated by Django 4.1.4 on 2023-01-21 07:53

import bboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0005_alter_additionalimage_options_alter_bb_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionalimage',
            options={'verbose_name': 'Дополнительное фото', 'verbose_name_plural': 'Дополнительные фото'},
        ),
        migrations.AlterField(
            model_name='additionalimage',
            name='image',
            field=models.ImageField(upload_to=bboard.models.get_timestamp_path, verbose_name='Дополнительное фото'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=bboard.models.get_timestamp_path, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[(None, 'Выберите пол'), ('m', 'М'), ('w', 'Ж')], default='m', max_length=1, null=True, verbose_name='Пол'),
        ),
    ]
