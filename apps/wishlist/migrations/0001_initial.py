# Generated by Django 3.2.7 on 2022-02-20 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('favourite_items', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(db_index=True, verbose_name='Quantity')),
                ('size', models.CharField(db_index=True, default='size', max_length=20, verbose_name='Size')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favourite_items.favouriteitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'wish',
            },
        ),
    ]
