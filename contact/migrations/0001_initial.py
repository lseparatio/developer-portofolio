# Generated by Django 4.1.3 on 2023-03-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('sent_message', models.CharField(max_length=10000)),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('sent_time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
    ]