# Generated by Django 4.1.4 on 2023-01-19 04:46

import bboard.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_bb_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='image',
            field=models.ImageField(blank=True, upload_to=bboard.models.get_timestamp_path, verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='AdditionalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=bboard.models.get_timestamp_path, verbose_name='Изображение')),
                ('bb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bboard.bb', verbose_name='Объявление')),
            ],
            options={
                'verbose_name': 'Дополнительная иллюстрация',
                'verbose_name_plural': 'Дополнительные иллюстрации',
            },
        ),
    ]