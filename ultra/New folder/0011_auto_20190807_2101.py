# Generated by Django 2.2.2 on 2019-08-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultra', '0010_auto_20190807_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_developer',
            name='profile_pic',
            field=models.FileField(blank=True, default='developerdp/default.jpg', null=True, upload_to='developerdp'),
        ),
    ]
