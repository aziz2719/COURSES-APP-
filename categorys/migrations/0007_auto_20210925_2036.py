# Generated by Django 3.2.7 on 2021-09-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorys', '0006_alter_contact_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='course',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='branches',
            field=models.ManyToManyField(related_name='branch1', to='categorys.Branch'),
        ),
        migrations.AddField(
            model_name='course',
            name='contacts',
            field=models.ManyToManyField(related_name='contact1', to='categorys.Contact'),
        ),
    ]
