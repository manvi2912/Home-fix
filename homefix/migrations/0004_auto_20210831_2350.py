# Generated by Django 3.2.6 on 2021-08-31 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homefix', '0003_contact_us_service_requested'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_provider',
            name='id',
        ),
        migrations.AlterField(
            model_name='service_provider',
            name='service_id',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
