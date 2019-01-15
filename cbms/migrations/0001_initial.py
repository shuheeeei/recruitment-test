# Generated by Django 2.1.5 on 2019-01-14 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('gender', models.CharField(choices=[('1', '女性'), ('2', '男性')], max_length=2, verbose_name='性別')),
                ('age', models.IntegerField(verbose_name='年齢')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default=['英語', 'ファイナンス', 'プログラミング'], max_length=30, verbose_name='科目')),
                ('base_fee', models.IntegerField(default=[5, 0, 20000], verbose_name='基本料金')),
                ('charge_fee', models.IntegerField(default=[3500, 3300, 3500], verbose_name='従量料金')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(verbose_name='受講時間')),
                ('date', models.DateField(verbose_name='受講日')),
                ('billing', models.IntegerField(verbose_name='請求書')),
                ('costomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbms.Costomer')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbms.Genre')),
            ],
        ),
    ]
