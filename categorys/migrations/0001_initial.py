# Generated by Django 3.2.7 on 2021-09-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=255, verbose_name='Широта')),
                ('longitude', models.CharField(max_length=255, verbose_name='Долгота')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Ветвь',
                'verbose_name_plural': 'Ветви',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='student_images', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(1, 'Телефон'), (2, 'Фейсбук'), (3, 'Электронная почта')], max_length=100)),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
