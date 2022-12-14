# Generated by Django 4.1.2 on 2022-12-23 04:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_project_app', '0003_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='order_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
