# Generated by Django 2.2.6 on 2022-02-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomendeditems', '0006_rename_image_recomendeditem_recomendedimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomendeditem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
