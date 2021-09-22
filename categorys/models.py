from django.db import models

class Category(models.Model):
    name = models.CharField('Название', max_length=255)
    image = models.ImageField('Фото', upload_to = 'student_images')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'

class Branch(models.Model):
    latitude = models.CharField('Широта', max_length=255)
    longitude = models.CharField('Долгота', max_length=255)
    address = models.CharField('Адрес', max_length=255)
    
    class Meta:
        verbose_name = 'Ветвь'
        verbose_name_plural = 'Ветви'

    def __str__(self):
        return f'{self.address}'


class Contact(models.Model):
    CHOICES = (
        ('1','Телефон'),
        ('2','Фейсбук'),
        ('3','Электронная почта'),
    )
    status = models.CharField(max_length=100, choices=CHOICES)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.status}'