# Generated by Django 4.2.7 on 2024-03-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposite_amount',
            name='depo_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
