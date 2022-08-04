# Generated by Django 4.0.6 on 2022-08-04 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tasks',
            field=models.ManyToManyField(to='todo.task'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
