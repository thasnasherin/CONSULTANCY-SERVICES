# Generated by Django 4.2.1 on 2024-04-16 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0007_ebooking_jid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebooking',
            name='uid',
        ),
    ]