# Generated by Django 4.2.7 on 2023-11-15 19:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('patronymic', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('current_profession', models.CharField(max_length=128)),
                ('work_experience', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU')),
            ],
        ),
    ]
