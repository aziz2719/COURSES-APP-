# Generated by Django 3.2.7 on 2021-09-25 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorys', '0007_auto_20210925_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='branches',
        ),
        migrations.RemoveField(
            model_name='course',
            name='contacts',
        ),
        migrations.AddField(
            model_name='branch',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch1', to='categorys.course'),
        ),
        migrations.AddField(
            model_name='contact',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact1', to='categorys.course'),
        ),
    ]
