# Generated by Django 4.2.5 on 2024-03-12 02:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("price", models.FloatField()),
                ("dis_price", models.FloatField()),
                ("category", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("image", models.CharField(max_length=4000)),
            ],
        ),
    ]
