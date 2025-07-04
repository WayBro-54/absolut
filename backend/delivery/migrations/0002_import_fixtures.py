# Generated by Django 5.2.3 on 2025-07-03 12:21
import os

from django.db import migrations

from backend import settings


def load_sql_file(filename):
    with open(filename, "r") as f:
        return f.read()


class Migration(migrations.Migration):

    dependencies = [
        ("delivery", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            sql=load_sql_file(
                os.path.join(settings.BASE_DIR, "delivery/fixtures/delivery.sql")
            ),
            reverse_sql=migrations.RunSQL.noop,
        )
    ]
