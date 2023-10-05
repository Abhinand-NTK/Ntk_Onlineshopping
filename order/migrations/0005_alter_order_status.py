# Generated by Django 4.2.4 on 2023-09-02 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Order confirmed', 'Order confirmed'), ('Return requested', 'Return requested'), ('Return processing', 'Return processing'), ('Out for delivery', 'Out for delivery'), ('Returned', 'Returned'), ('Cancelled', 'Cancelled'), ('Shipped', 'Shipped')], default='Order Confirmed', max_length=50),
        ),
    ]