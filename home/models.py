from django.db import models

# Create your models here.

class Doctor(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    position = models.CharField(max_length=300, verbose_name="Должность")
    image = models.ImageField(null=True, blank=True, upload_to="doctors")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Доктора'
        ordering = ['full_name']


class Description(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="descriptions")
    text = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Описание_врачей'
        ordering = ['text']


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Новости")
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="news")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        ordering = ['title']

class Fulldescription(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="news_descriptions")
    text = models.TextField(verbose_name="Текст")

    class Meta:
        verbose_name = 'Описание_новостей'
        ordering = ['text']



class Treatment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Диагноз")
    image = models.ImageField(null=True, blank=True, upload_to="treatment")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Диагноз'
        ordering = ['title']

class TreatmentFullDescription(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, related_name="treatment_descriptions")
    title = models.CharField(max_length=200, verbose_name="Заглавие", blank=True, null=True)
    text = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Описание_лечения'
        ordering = ['text']

class Surgery(models.Model):
    title = models.CharField(max_length=200, verbose_name="Операции")
    image = models.ImageField(null=True, blank=True, upload_to="surgery")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Операции'
        ordering = ['title']


class SurgeryFullDescription(models.Model):
    treatment = models.ForeignKey(Surgery, on_delete=models.CASCADE, related_name="surgery_descriptions")
    title = models.CharField(max_length=200, verbose_name="Заглавие", blank=True, null=True)
    text = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Описание_операция'
        ordering = ['text']




class FAQ(models.Model):
    question = models.CharField(max_length=300, verbose_name="вопросы",)
    answer = models.TextField(verbose_name="ответы")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопросы'
        ordering = ['question']

class Reviews(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    image = models.ImageField(null=True, blank=True, upload_to="reviews")
    text = models.TextField(verbose_name="отзывы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзывы'
        ordering = ['name']


class VideoContent(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название_видео", blank=True, null=True)
    file = models.FileField(upload_to="video", verbose_name="видео")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео_Контент'
        ordering = ['title']


class ImagesContent(models.Model):
    title = models.CharField(max_length=100, verbose_name="Картинка", blank=True, null=True)
    file = models.ImageField(null=True, blank=True, upload_to="work_images")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея_Контент'
        ordering = ['title']


