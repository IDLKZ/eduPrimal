from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.db.models import *



# Create your models here.

# КАТЕГОРИЯ
class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Описание", help_text="Необязательное поле")
    status = models.BooleanField(default=True, verbose_name="Активный")
    image = models.ImageField(upload_to="uploads/category", blank=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Обновлен")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория курсов'
        verbose_name_plural = "Категории курсов"
        ordering = ["title"]

    def get_image(self):
        if self.image:
            return format_html('<img src="{}" width="auto" height="150px" />'.format(self.image.url))
        else:
            return format_html('<img src="{}" width="auto" height="150px" />'.format('https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX24139876.jpg'))
    get_image.short_description = "Миниатюра изображения"


# Тэги

class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Наименование тэга")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    status = models.BooleanField(default=True, verbose_name="Активный")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = "Тэги курсов"
        ordering = ["title"]


class Language(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Язык курса")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = "Языки курсов"
        ordering = ["title"]


# Автор


class Author(models.Model):
    title = models.CharField(max_length=255, verbose_name="Автор курса")
    profession = models.CharField(max_length=255,verbose_name="Профессианальная компетенция")
    description = models.TextField(blank=True, verbose_name="Описание", help_text="Необязательное поле", )
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    status = models.BooleanField(default=True, verbose_name="Активный")
    image = models.ImageField(upload_to="uploads/author", blank=True, verbose_name="Изображение")
    instagram = models.URLField(verbose_name="Соц сеть Инстаграм",blank=True)
    facebook = models.URLField(verbose_name="Соц сеть Facebook",blank=True)
    linkedin = models.URLField(verbose_name="LinkedIn",blank=True)
    vk = models.URLField(verbose_name="Соц сеть VK",blank=True)
    twitter = models.URLField(verbose_name="Соц сеть twitter",blank=True)
    postbox = models.URLField(verbose_name="Почта",blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return format_html('<img src="{}" width="auto" height="150px" />'.format(self.image.url))
        else:
            return format_html('<img src="{}" width="auto" height="150px" />'.format('https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX24139876.jpg'))
    get_image.short_description = "Миниатюра изображения"


    def get_courses_count(self):
        return self.courses.count()

    def get_lessons_count(self):
        return self.courses.aggregate(Count('lessons'))["lessons__count"]

    def get_imageUrl(self):
        if self.image:
            return self.image.url
        else:
            return 'https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX24139876.jpg'

    def get_absolute_url(self):
        return reverse('singleAuthor',kwargs={"slug":self.slug})


    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = "Авторы"
        ordering = ["title"]

# Курсы
class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование курса")
    subtitle = models.CharField(max_length=255, verbose_name="Подтекст курса")
    image = models.ImageField(upload_to="uploads/course", blank=True, verbose_name="Изображение")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    video_url = models.URLField(max_length=500,blank=True,verbose_name="Видео курса")
    description = models.TextField( verbose_name="Описание")
    advantages = models.TextField(blank=True,verbose_name="Преимущества курса")
    language = models.ForeignKey(Language,on_delete=models.PROTECT, blank=True,related_name="language",verbose_name="Язык курса")
    category = models.ForeignKey(Category,on_delete=models.PROTECT, blank=True,related_name="category",verbose_name="Категория курса")
    authors = models.ManyToManyField(Author, blank=True,verbose_name="Авторы курса",related_name="courses")
    tags = models.ManyToManyField(Tag, blank=True,verbose_name="Тэги",related_name="courses")
    status = models.BooleanField(default=True, verbose_name="Активный")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(verbose_name="Дата публикации")

    def get_image(self):
        if self.image:
            return format_html('<img src="{}" width="auto" height="150px" />'.format(self.image.url))
        else:
            return format_html('<img src="{}" width="auto" height="150px" />'.format('https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX24139876.jpg'))
    get_image.short_description = "Миниатюра изображения"

    def get_absolute_url(self):
        return reverse('singleCourse',kwargs={"slug":self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = "Курсы"
        ordering = ["-published"]


class Lesson(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="Курс",related_name="lessons")
    title = models.CharField(max_length=255, verbose_name="Наименование курса")
    subtitle = models.CharField(max_length=255, verbose_name="Подтекст курса")
    image = models.ImageField(upload_to="uploads/lesson/image", blank=True, verbose_name="Изображение")
    file = models.ImageField(upload_to="uploads/lesson/file", blank=True, verbose_name="Дополнительный файл")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    video_url = models.URLField(max_length=500, blank=True, verbose_name="Видеоурок")
    description = models.TextField(verbose_name="Описание")
    order = models.IntegerField(verbose_name="Порядковый номер",)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('singleLesson',kwargs={"slug":self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видеоурок'
        verbose_name_plural = "Видеоуроки"
        ordering = ["order"]


class Quiz(models.Model):
        title = models.CharField(max_length=255, verbose_name="Наименование теста")
        slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
        lessons = models.ManyToManyField(Lesson,related_name="quizzes")


        def __str__(self):
            return self.title

        class Meta:
            verbose_name = 'Тест'
            verbose_name_plural = "Тесты"


class Question(models.Model):
        answers = [('A', 'Ответ А'),('B', 'Ответ B'),('C', 'Ответ C'),('D', 'Ответ D'),('E', 'Ответ E'),]
        title = models.CharField(max_length=255, verbose_name="Вопрос")
        question_image = models.ImageField(blank=True, upload_to="questions",verbose_name="Файл к вопросу")
        quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,verbose_name="Экзамен")
        A = models.CharField(max_length=255, verbose_name="Вопрос А")
        question_A = models.ImageField(blank=True, upload_to="questions",verbose_name="Файл к Вопрос А")
        B = models.CharField(max_length=255, verbose_name="Вопрос B")
        question_B = models.ImageField(blank=True, upload_to="questions",verbose_name="Файл к Вопрос B")
        C = models.CharField(max_length=255, verbose_name="Вопрос C")
        question_C = models.ImageField(blank=True, upload_to="questions",verbose_name="Файл к Вопрос C")
        D = models.CharField(max_length=255, verbose_name="Вопрос D")
        question_D = models.ImageField(blank=True, upload_to="questions",verbose_name="Файл к Вопрос D")
        E = models.CharField(max_length=255, verbose_name="Вопрос E")
        question_E = models.ImageField(blank=True,upload_to="questions",verbose_name="Файл к Вопрос E")
        answer = models.CharField(max_length=255,choices=answers,default="A",verbose_name="Ответ")


        def __str__(self):
            return self.title

        class Meta:
            verbose_name = 'Вопрос'
            verbose_name_plural = "Вопросы"
