# Generated by Django 3.2.9 on 2022-07-04 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20220704_0620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='surgery',
            options={'ordering': ['title'], 'verbose_name': 'Операции'},
        ),
        migrations.RenameField(
            model_name='surgeryfulldescription',
            old_name='treatment',
            new_name='surgery',
        ),
    ]