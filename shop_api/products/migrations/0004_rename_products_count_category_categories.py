# Generated by Django 5.0.7 on 2024-07-13 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_products_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='products_count',
            new_name='categories',
        ),
    ]
