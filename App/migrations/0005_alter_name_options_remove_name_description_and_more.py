# Generated by Django 4.0.2 on 2022-02-27 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_alter_name_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='name',
            options={'verbose_name': 'заказ', 'verbose_name_plural': 'заказы'},
        ),
        migrations.RemoveField(
            model_name='name',
            name='description',
        ),
        migrations.AddField(
            model_name='name',
            name='work1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='name',
            name='work2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='name',
            name='work3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='name',
            name='work4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='name',
            name='work5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='name',
            name='work6',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='name',
            name='email',
            field=models.CharField(max_length=100, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='name',
            name='name',
            field=models.CharField(max_length=100, verbose_name='имя_фамилия'),
        ),
    ]
