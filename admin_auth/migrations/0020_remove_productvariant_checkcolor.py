# Generated by Django 4.2.4 on 2023-09-21 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_auth', '0019_productvariant_checkcolor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='checkcolor',
        ),
    ]
