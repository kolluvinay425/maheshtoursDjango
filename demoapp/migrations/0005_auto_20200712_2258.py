# Generated by Django 3.0.5 on 2020-07-12 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0004_auto_20200501_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(default='Image-Coming-Soon.jpg', upload_to='media'),
        ),
    ]