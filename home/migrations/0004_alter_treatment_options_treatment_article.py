# Generated by Django 4.0.5 on 2022-07-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220712_1505'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='treatment',
            options={'ordering': ['article'], 'verbose_name': 'Диагноз'},
        ),
        migrations.AddField(
            model_name='treatment',
            name='article',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
