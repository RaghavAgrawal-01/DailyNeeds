# Generated by Django 5.0.6 on 2024-07-28 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailylist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
    ]