from django.db import models

# Create your models here.

class Doctor(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    position = models.CharField(max_length=300, verbose_name="Должность")
    image = models.ImageField(null=True, blank=True, upload_to="doctors")

    def __str__(self):
        return self.full_name


class Description(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="descriptions")
    text = models.TextField(verbose_name="Описание")


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Новости")
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="news")

    def __str__(self):
        return self.title

class Fulldescription(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="news_descriptions")
    text = models.TextField(verbose_name="Текст")


<<<<<<< HEAD

class Treatment(models.Model):
    title = models.CharField(max_length=200, verbose_name="Диагноз")
    image = models.ImageField(null=True, blank=True, upload_to="treatment")
=======
class Headlines(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заглавки")
    image = models.ImageField(null=True, blank=True, upload_to="headlines")
>>>>>>> edd88213fccf6084ad3678df96b7d4c8e0477a8d

    def __str__(self):
        return self.title

<<<<<<< HEAD
class TreatmentFullDescription(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, related_name="treatment_descriptions")
    title = models.CharField(max_length=200, verbose_name="Заглавие", blank=True, null=True)
    text = models.TextField(verbose_name="Описание")


class FAQ(models.Model):
    question = models.CharField(max_length=300, verbose_name="вопросы",)
    answer = models.TextField(verbose_name="ответы")

    def __str__(self):
        return self.question


=======
class DescriptionHeadlines(models.Model):
    headlines = models.ForeignKey(Headlines, on_delete=models.CASCADE, related_name="headlines_description")
    text = models.TextField(verbose_name="Текст")

    
>>>>>>> edd88213fccf6084ad3678df96b7d4c8e0477a8d
