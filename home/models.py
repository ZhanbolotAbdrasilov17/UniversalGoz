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

