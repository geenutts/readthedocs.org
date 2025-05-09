# Generated by Django 1.11.16 on 2018-10-31 11:25
from django.db import migrations
from django.db import models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("gold", "0002_rename_last_4_digits"),
    ]

    operations = [
        migrations.AlterField(
            model_name="golduser",
            name="level",
            field=models.CharField(
                choices=[
                    ("v1-org-5", "$5/mo"),
                    ("v1-org-10", "$10/mo"),
                    ("v1-org-15", "$15/mo"),
                    ("v1-org-20", "$20/mo"),
                    ("v1-org-50", "$50/mo"),
                    ("v1-org-100", "$100/mo"),
                ],
                default="v1-org-5",
                max_length=20,
                verbose_name="Level",
            ),
        ),
    ]
