# Generated by Django 2.1.5 on 2019-01-27 13:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbms', '0006_auto_20190127_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costomer',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(79)], verbose_name='年齢'),
        ),
        migrations.AlterField(
            model_name='costomer',
            name='gender',
            field=models.CharField(choices=[('1', '女性'), ('2', '男性')], max_length=2, verbose_name='性別'),
        ),
    ]
