# Generated by Django 4.0.5 on 2022-07-04 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20220704_0714'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='surgery',
            options={'ordering': ['title'], 'verbose_name': 'Операция'},
        ),
        migrations.RenameField(
            model_name='surgeryfulldescription',
            old_name='surgery',
            new_name='treatment',
        ),
    ]
