# Generated by Django 4.2.4 on 2023-10-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_auth', '0023_customuser_referral_code_customuser_referrer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='images',
            field=models.ImageField(blank=True, upload_to='photos/userprofile'),
        ),
    ]
