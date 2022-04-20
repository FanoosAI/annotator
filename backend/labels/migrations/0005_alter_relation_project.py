# Generated by Django 3.2.11 on 2022-02-04 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("projects", "0002_auto_20220204_0201"),
        ("labels", "0004_auto_20220128_0246"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name="relation",
                    name="project",
                    field=models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="annotation_relations",
                        to="projects.project",
                    ),
                ),
            ],
            database_operations=[],
        )
    ]
