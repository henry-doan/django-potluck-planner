# Generated by Django 3.2.9 on 2021-11-19 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20211119_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='pictures/noimg.jpg', upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='pictures/noimg.jpg', upload_to='pictures'),
        ),
    ]
