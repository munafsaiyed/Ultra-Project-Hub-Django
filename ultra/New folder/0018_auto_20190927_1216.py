# Generated by Django 2.2.2 on 2019-09-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultra', '0017_auto_20190927_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_client',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
