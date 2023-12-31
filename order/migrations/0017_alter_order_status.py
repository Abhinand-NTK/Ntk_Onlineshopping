# Generated by Django 4.2.4 on 2023-09-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Shipped', 'Shipped'), ('Cancelled', 'Cancelled'), ('Return processing', 'Return processing'), ('Returned', 'Returned'), ('Out for delivery', 'Out for delivery'), ('Order confirmed', 'Order confirmed'), ('Return requested', 'Return requested'), ('Delivered', 'Delivered')], default='Order Confirmed', max_length=50),
        ),
    ]
