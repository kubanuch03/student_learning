# Generated by Django 3.2.3 on 2021-06-19 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizzes',
            name='time_limit_mins',
        ),
    ]