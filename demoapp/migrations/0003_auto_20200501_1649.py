# Generated by Django 2.2 on 2020-05-01 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_remove_tour_catagory_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='demoapp.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='demoapp/'),
        ),
    ]
