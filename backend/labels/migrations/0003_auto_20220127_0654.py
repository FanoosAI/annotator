# Generated by Django 3.2.11 on 2022-01-27 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("label_types", "0001_initial"),
        ("labels", "0002_rename_annotationrelations_relation"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name="category",
                    name="label",
                    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="label_types.categorytype"),
                ),
                migrations.AlterField(
                    model_name="relation",
                    name="type",
                    field=models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="annotation_relations",
                        to="label_types.relationtypes",
                    ),
                ),
                migrations.AlterField(
                    model_name="span",
                    name="label",
                    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="label_types.spantype"),
                ),
            ]
        )
    ]
