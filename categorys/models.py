from django.db import models

class Category(models.Model):
    name = models.CharField('Название', max_length=255)
    image = models.ImageField('Фото', upload_to = 'images')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    name = models.CharField('Название курса', max_length=255, null=True)
    description = models.CharField('Описание курса', max_length=255, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category1', null=True)
    logo = models.ImageField('logo/', upload_to='media', null=True)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name
    


class Branch(models.Model):
    latitude = models.CharField('Широта', max_length=255)
    longitude = models.CharField('Долгота', max_length=255)
    address = models.CharField('Адрес', max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branch1', null=True)

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
    value = models.CharField(max_length=200, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contact1', null=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.status}'