# Generated by Django 3.2.6 on 2021-11-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homefix', '0010_alter_service_requested_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
