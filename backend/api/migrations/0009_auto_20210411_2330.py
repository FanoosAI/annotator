# Generated by Django 3.1.7 on 2021-04-11 23:30

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("api", "0008_auto_20210302_1013"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="meta",
            field=models.JSONField(default=dict),
        ),
    ]
