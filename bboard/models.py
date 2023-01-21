from django.db import models
from datetime import datetime
from os.path import splitext

def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])

# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления')
    rubric = models.ForeignKey('Rubric', null = True, on_delete=models.PROTECT, verbose_name='Категория')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Фото', null=True)
    class Kinds(models.TextChoices):
        MAN = 'm', 'М'
        WOMAN = 'w', 'Ж'
        __empty__ = 'Выберите пол'
    kind = models.CharField(null=True, max_length=1, choices=Kinds.choices, default=Kinds.MAN, verbose_name='Пол')

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Лицо'
        verbose_name_plural = 'Лица'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(verbose_name='Название', db_index = True, max_length=20)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

class AdditionalImage(models.Model):
    bb = models.ForeignKey(Bb, on_delete=models.CASCADE, verbose_name='Лицо')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Дополнительное фото')

    class Meta:
        verbose_name_plural = 'Дополнительные фото'
        verbose_name = 'Дополнительное фото'

