# Generated by Django 2.2.6 on 2019-10-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191022_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='img/default.jpg', null=True, upload_to='user_image/'),
        ),
    ]
