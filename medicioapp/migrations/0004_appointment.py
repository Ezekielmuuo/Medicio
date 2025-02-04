# Generated by Django 5.0.6 on 2024-07-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicioapp', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('department', models.CharField(max_length=50)),
                ('doctor', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
