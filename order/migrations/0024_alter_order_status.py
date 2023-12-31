# Generated by Django 4.2.4 on 2023-09-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0023_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Returned', 'Returned'), ('Return processing', 'Return processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Order confirmed', 'Order confirmed'), ('Cancelled', 'Cancelled'), ('Return requested', 'Return requested'), ('Out for delivery', 'Out for delivery')], default='Order Confirmed', max_length=50),
        ),
    ]
