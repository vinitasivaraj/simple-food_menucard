# Generated by Django 3.2.8 on 2023-01-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='mysite/pictures/profile.png', upload_to='profile_images'),
        ),
    ]
