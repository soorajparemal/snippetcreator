# Generated by Django 2.2 on 2021-11-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retriever', '0003_auto_20211128_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
