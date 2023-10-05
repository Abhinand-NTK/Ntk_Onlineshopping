# Generated by Django 4.2.4 on 2023-09-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Out for delivery', 'Out for delivery'), ('Order confirmed', 'Order confirmed'), ('Return requested', 'Return requested'), ('Returned', 'Returned'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Return processing', 'Return processing')], default='Order Confirmed', max_length=50),
        ),
    ]