# Generated by Django 5.0 on 2023-12-18 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_project_products', '0006_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='review_images/'),
        ),
    ]