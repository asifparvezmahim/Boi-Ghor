# Generated by Django 4.2.7 on 2024-03-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowing_price',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=10000),
        ),
    ]
