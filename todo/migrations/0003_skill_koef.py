# Generated by Django 4.0.3 on 2022-04-05 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_skill_special_employes'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='koef',
            field=models.FloatField(default=1, verbose_name='Коэффициент'),
            preserve_default=False,
        ),
    ]