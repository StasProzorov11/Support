# Generated by Django 5.0.3 on 2024-03-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Issue",
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
                ("junior_id", models.IntegerField()),
                ("senior_id", models.IntegerField()),
                ("title", models.CharField(max_length=100)),
                ("body", models.TextField()),
            ],
        ),
    ]
