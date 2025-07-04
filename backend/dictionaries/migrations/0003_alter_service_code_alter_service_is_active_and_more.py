# Generated by Django 5.2.3 on 2025-07-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dictionaries", "0002_load_init_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="code",
            field=models.CharField(
                max_length=255, unique=True, verbose_name="Код услуги"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Активна"),
        ),
        migrations.AlterField(
            model_name="service",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Имя услуги"),
        ),
        migrations.AlterField(
            model_name="statusdelivery",
            name="code",
            field=models.CharField(
                max_length=255, unique=True, verbose_name="Код статуса"
            ),
        ),
        migrations.AlterField(
            model_name="statusdelivery",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Активна"),
        ),
        migrations.AlterField(
            model_name="statusdelivery",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Статус доставки"),
        ),
    ]
