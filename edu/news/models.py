from django.db import models


# Create your models here.

class CategoryNews(models.Model):
    title = models.CharField(max_length=255,verbose_name="Категория новостей")
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = "Категория новостей"

class News(models.Model):
    category = models.ForeignKey(CategoryNews, on_delete=models.CASCADE, related_name="news",verbose_name="Категория новостей")
    type = models.IntegerField(choices=((1,"НОВОСТЬ"),(2,"БЛОГ")),verbose_name="Тип новости")
    thumbnail = models.ImageField(upload_to="news/images", max_length=255,verbose_name="Предпросмотр изображения")
    image = models.ImageField(upload_to="news/images", max_length=255,verbose_name="Изображения")
    title = models.CharField(max_length=255,verbose_name="Наименование")
    slug = models.SlugField(max_length=255,verbose_name="Ссылка")
    author = models.CharField(max_length=255,verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    status = models.BooleanField(default=True,verbose_name="Статус")
    published = models.DateTimeField(verbose_name="Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость и блог'
        verbose_name_plural = "Новости и блоги"


