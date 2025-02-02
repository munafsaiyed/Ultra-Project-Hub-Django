# Generated by Django 2.2.2 on 2019-08-01 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('Aid', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('projdesc', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='pictures')),
                ('language', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registration_client',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('gender', models.CharField(blank=True, max_length=200, null=True)),
                ('dob', models.DateField(default='')),
                ('email', models.CharField(max_length=100)),
                ('contact', models.BigIntegerField(blank=True, default=0, null=True)),
                ('password', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=200)),
                ('addresh', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration_developer',
            fields=[
                ('Did', models.AutoField(primary_key=True, serialize=False)),
                ('Dname', models.CharField(max_length=200)),
                ('gender', models.CharField(blank=True, max_length=200, null=True)),
                ('dob', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('contact', models.BigIntegerField(blank=True, default=0, null=True)),
                ('password', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=200)),
                ('addresh', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.IntegerField(blank=True, default=0, null=True)),
                ('skill', models.CharField(max_length=200)),
                ('experience', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='noti_developer',
            fields=[
                ('noti_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('recev_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultra.Registration_developer')),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultra.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='bid',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField(default=0)),
                ('days', models.IntegerField(default=0)),
                ('date_time', models.DateTimeField()),
                ('Did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultra.Registration_developer')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultra.Project')),
            ],
        ),
    ]
