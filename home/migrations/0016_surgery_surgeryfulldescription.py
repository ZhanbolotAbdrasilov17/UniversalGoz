<<<<<<< HEAD

=======
>>>>>>> 65f2247ef83f7c50880a76e780102b722ad065ed
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20220702_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Операции')),
                ('image', models.ImageField(blank=True, null=True, upload_to='surgery')),
            ],
            options={
                'verbose_name': 'Операция',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='SurgeryFullDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заглавие')),
                ('text', models.TextField(verbose_name='Описание')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surgery_descriptions', to='home.surgery')),
            ],
            options={
                'verbose_name': 'Описание_операция',
                'ordering': ['text'],
            },
        ),
    ]
