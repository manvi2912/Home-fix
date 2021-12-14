# Generated by Django 3.2.6 on 2021-09-25 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homefix', '0007_auto_20210925_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='contact_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='service_requested',
            name='customer_contact_no',
            field=models.CharField(max_length=10),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=200)),
                ('rating', models.IntegerField(null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homefix.service_provider')),
            ],
        ),
    ]