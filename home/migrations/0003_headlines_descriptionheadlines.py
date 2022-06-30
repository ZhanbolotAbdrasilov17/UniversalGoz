# Generated by Django 4.0.5 on 2022-06-26 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_news_fulldescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headlines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заглавки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='headlines')),
            ],
        ),
        migrations.CreateModel(
            name='DescriptionHeadlines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('headlines', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='headlines_description', to='home.headlines')),
            ],
        ),
    ]
