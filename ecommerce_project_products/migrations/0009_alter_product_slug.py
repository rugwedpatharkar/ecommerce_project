# Generated by Django 5.0 on 2023-12-24 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_project_products', '0008_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
