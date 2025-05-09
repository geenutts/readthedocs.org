# Generated by Django 1.11.16 on 2018-11-02 13:24
import jsonfield.fields
from django.db import migrations
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("builds", "0005_remove-version-alias"),
    ]

    operations = [
        migrations.AddField(
            model_name="build",
            name="_config",
            field=jsonfield.fields.JSONField(
                default=dict, verbose_name="Configuration used in the build"
            ),
        ),
    ]
