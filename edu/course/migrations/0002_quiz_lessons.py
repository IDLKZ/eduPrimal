# Generated by Django 3.2.9 on 2021-11-28 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='lessons',
            field=models.ManyToManyField(related_name='lessons', to='course.Lesson'),
        ),
    ]