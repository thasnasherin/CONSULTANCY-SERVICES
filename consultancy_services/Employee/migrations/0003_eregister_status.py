# Generated by Django 4.2.1 on 2024-04-16 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_eregister_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='eregister',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
