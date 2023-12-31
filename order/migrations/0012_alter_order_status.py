# Generated by Django 4.2.4 on 2023-09-20 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Shipped', 'Shipped'), ('Order confirmed', 'Order confirmed'), ('Returned', 'Returned'), ('Return processing', 'Return processing'), ('Return requested', 'Return requested'), ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered')], default='Order Confirmed', max_length=50),
        ),
    ]
