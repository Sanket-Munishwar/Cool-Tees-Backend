# Generated by Django 4.1.3 on 2022-11-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_auto_20220227_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
