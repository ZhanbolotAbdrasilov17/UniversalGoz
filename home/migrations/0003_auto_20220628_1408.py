# Generated by Django 3.2.9 on 2022-06-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_news_fulldescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='position_ky',
            field=models.CharField(max_length=300, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='position_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Должность'),
        ),
    ]
