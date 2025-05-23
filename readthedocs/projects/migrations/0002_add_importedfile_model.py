from django.db import migrations
from django.db import models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("builds", "0001_initial"),
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImportedFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                ("slug", models.SlugField(verbose_name="Slug")),
                ("path", models.CharField(max_length=255, verbose_name="Path")),
                ("md5", models.CharField(max_length=255, verbose_name="MD5 checksum")),
                ("commit", models.CharField(max_length=255, verbose_name="Commit")),
                (
                    "project",
                    models.ForeignKey(
                        related_name="imported_files",
                        verbose_name="Project",
                        to="projects.Project",
                        on_delete=models.CASCADE,
                    ),
                ),
                (
                    "version",
                    models.ForeignKey(
                        related_name="imported_files",
                        verbose_name="Version",
                        to="builds.Version",
                        null=True,
                        on_delete=models.CASCADE,
                    ),
                ),
            ],
        ),
    ]
