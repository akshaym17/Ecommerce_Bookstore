# Generated by Django 4.2.7 on 2023-12-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(default=True),
        ),
    ]