# Generated by Django 4.0.3 on 2022-04-05 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_skill_koef'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('cost', models.IntegerField(verbose_name='Стоимость лечения')),
            ],
        ),
    ]
