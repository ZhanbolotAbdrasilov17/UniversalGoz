# Generated by Django 3.2.9 on 2022-07-12 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('position', models.CharField(max_length=300, verbose_name='Должность')),
                ('position_ru', models.CharField(max_length=300, null=True, verbose_name='Должность')),
                ('position_ky', models.CharField(max_length=300, null=True, verbose_name='Должность')),
                ('image', models.ImageField(blank=True, null=True, upload_to='doctors')),
            ],
            options={
                'verbose_name': 'Доктора',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300, verbose_name='вопросы')),
                ('question_ru', models.CharField(max_length=300, null=True, verbose_name='вопросы')),
                ('question_ky', models.CharField(max_length=300, null=True, verbose_name='вопросы')),
                ('answer', models.TextField(verbose_name='ответы')),
                ('answer_ru', models.TextField(null=True, verbose_name='ответы')),
                ('answer_ky', models.TextField(null=True, verbose_name='ответы')),
            ],
            options={
                'verbose_name': 'Вопросы',
                'ordering': ['question'],
            },
        ),
        migrations.CreateModel(
            name='ImagesContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Картинка')),
                ('title_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='Картинка')),
                ('title_ky', models.CharField(blank=True, max_length=100, null=True, verbose_name='Картинка')),
                ('file', models.ImageField(blank=True, null=True, upload_to='work_images')),
            ],
            options={
                'verbose_name': 'Галерея_Контент',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Новости')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Новости')),
                ('title_ky', models.CharField(max_length=200, null=True, verbose_name='Новости')),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news')),
            ],
            options={
                'verbose_name': 'Новости',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('image', models.ImageField(blank=True, null=True, upload_to='reviews')),
                ('text', models.TextField(verbose_name='отзывы')),
                ('text_ru', models.TextField(null=True, verbose_name='отзывы')),
                ('text_ky', models.TextField(null=True, verbose_name='отзывы')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Операции')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Операции')),
                ('title_ky', models.CharField(max_length=200, null=True, verbose_name='Операции')),
                ('image', models.ImageField(blank=True, null=True, upload_to='surgery')),
                ('my_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Операции',
                'ordering': ['my_id'],
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Диагноз')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Диагноз')),
                ('title_ky', models.CharField(max_length=200, null=True, verbose_name='Диагноз')),
                ('image', models.ImageField(blank=True, null=True, upload_to='treatment')),
                ('my_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Диагноз',
                'ordering': ['my_id'],
            },
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название_видео')),
                ('title_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название_видео')),
                ('title_ky', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название_видео')),
                ('file', models.FileField(upload_to='video', verbose_name='видео')),
                ('image', models.ImageField(blank=True, null=True, upload_to='content')),
            ],
            options={
                'verbose_name': 'Видео_Контент',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='TreatmentFullDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заглавие')),
                ('title_ru', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заглавие')),
                ('title_ky', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заглавие')),
                ('text', models.TextField(verbose_name='Описание')),
                ('text_ru', models.TextField(null=True, verbose_name='Описание')),
                ('text_ky', models.TextField(null=True, verbose_name='Описание')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatment_descriptions', to='home.treatment')),
            ],
            options={
                'verbose_name': 'Описание_лечения',
            },
        ),
        migrations.CreateModel(
            name='SurgeryFullDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заглавие')),
                ('title_ru', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заглавие')),
                ('title_ky', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заглавие')),
                ('text', models.TextField(verbose_name='Описание')),
                ('text_ru', models.TextField(null=True, verbose_name='Описание')),
                ('text_ky', models.TextField(null=True, verbose_name='Описание')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surgery_descriptions', to='home.surgery')),
            ],
            options={
                'verbose_name': 'Описание_операция',
            },
        ),
        migrations.CreateModel(
            name='Fulldescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('text_ru', models.TextField(null=True, verbose_name='Текст')),
                ('text_ky', models.TextField(null=True, verbose_name='Текст')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_descriptions', to='home.news')),
            ],
            options={
                'verbose_name': 'Описание_новостей',
                'ordering': ['text'],
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Описание')),
                ('text_ru', models.TextField(null=True, verbose_name='Описание')),
                ('text_ky', models.TextField(null=True, verbose_name='Описание')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='home.doctor')),
            ],
            options={
                'verbose_name': 'Описание_врачей',
                'ordering': ['text'],
            },
        ),
    ]
