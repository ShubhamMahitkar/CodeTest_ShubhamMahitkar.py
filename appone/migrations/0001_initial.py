# Generated by Django 2.2.12 on 2020-10-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
