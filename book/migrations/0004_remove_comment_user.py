# Generated by Django 4.2.7 on 2024-03-24 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
