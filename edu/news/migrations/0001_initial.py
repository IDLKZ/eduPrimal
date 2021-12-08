# Generated by Django 3.2.9 on 2021-12-05 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Категория новостей')),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория новости',
                'verbose_name_plural': 'Категория новостей',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'НОВОСТЬ'), (2, 'БЛОГ')], verbose_name='Тип новости')),
                ('thumbnail', models.ImageField(max_length=255, upload_to='news/images', verbose_name='Предпросмотр изображения')),
                ('image', models.ImageField(max_length=255, upload_to='news/images', verbose_name='Изображения')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=255, verbose_name='Ссылка')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.BooleanField(default=True, verbose_name='Статус')),
                ('published', models.DateTimeField(verbose_name='Дата публикации')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='news.categorynews', verbose_name='Категория новостей')),
            ],
            options={
                'verbose_name': 'Новость и блог',
                'verbose_name_plural': 'Новости и блоги',
            },
        ),
    ]