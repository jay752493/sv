# Generated by Django 4.1.4 on 2023-01-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0006_alter_additionalimage_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='firstname',
            field=models.CharField(max_length=50, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='bb',
            name='midname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
    ]
