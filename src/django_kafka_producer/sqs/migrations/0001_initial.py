# Generated by Django 2.2.7 on 2019-11-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Default',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_number', models.CharField(max_length=100)),
                ('second_number', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=100)),
            ],
        ),
    ]
