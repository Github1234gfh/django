# Generated by Django 4.1.4 on 2023-01-04 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Категории')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_book', models.CharField(max_length=50, verbose_name='Назване книги')),
                ('autor', models.CharField(max_length=100, verbose_name='Автор')),
                ('date', models.DateField(verbose_name='Дата издания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.category')),
            ],
        ),
    ]
