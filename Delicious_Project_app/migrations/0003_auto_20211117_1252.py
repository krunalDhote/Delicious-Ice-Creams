# Generated by Django 3.2.6 on 2021-11-17 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Delicious_Project_app', '0002_signin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signin',
            name='address',
        ),
        migrations.RemoveField(
            model_name='signin',
            name='email',
        ),
        migrations.RemoveField(
            model_name='signin',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='signin',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='signin',
            name='password',
        ),
        migrations.RemoveField(
            model_name='signin',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='signin',
            name='username',
        ),
    ]
