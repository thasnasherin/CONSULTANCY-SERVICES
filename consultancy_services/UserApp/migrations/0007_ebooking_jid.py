# Generated by Django 4.2.1 on 2024-04-16 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0005_delete_service'),
        ('UserApp', '0006_booking_status_ebooking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebooking',
            name='jid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminApp.job'),
        ),
    ]