# Generated by Django 3.2.7 on 2021-09-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorys', '0008_auto_20210925_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('1', 'Телефон'), ('2', 'Фейсбук'), ('3', 'Электронная почта')], max_length=100),
        ),
    ]
