# Generated by Django 3.2.11 on 2022-02-04 02:01

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("api", "0035_auto_20220128_0246"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name="imageclassificationproject",
                    name="project_ptr",
                ),
                migrations.RemoveField(
                    model_name="intentdetectionandslotfillingproject",
                    name="project_ptr",
                ),
                migrations.RemoveField(
                    model_name="project",
                    name="created_by",
                ),
                migrations.RemoveField(
                    model_name="project",
                    name="polymorphic_ctype",
                ),
                migrations.RemoveField(
                    model_name="seq2seqproject",
                    name="project_ptr",
                ),
                migrations.RemoveField(
                    model_name="sequencelabelingproject",
                    name="project_ptr",
                ),
                migrations.RemoveField(
                    model_name="speech2textproject",
                    name="project_ptr",
                ),
                migrations.RemoveField(
                    model_name="tag",
                    name="project",
                ),
                migrations.RemoveField(
                    model_name="textclassificationproject",
                    name="project_ptr",
                ),
            ],
            database_operations=[],
        )
    ]
