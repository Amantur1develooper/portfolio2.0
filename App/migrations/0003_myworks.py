# Generated by Django 4.0.2 on 2022-02-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('link', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
