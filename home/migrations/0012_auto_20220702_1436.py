# Generated by Django 3.2.9 on 2022-07-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20220630_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatmentfulldescription',
            name='title_ky',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заглавие'),
        ),
        migrations.AddField(
            model_name='treatmentfulldescription',
            name='title_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Заглавие'),
        ),
    ]