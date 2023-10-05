# Generated by Django 4.2.4 on 2023-09-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='retrunsingleordernote',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Returned', 'Returned'), ('Return requested', 'Return requested'), ('Order confirmed', 'Order confirmed'), ('Shipped', 'Shipped'), ('Return processing', 'Return processing')], default='Order Confirmed', max_length=50),
        ),
    ]