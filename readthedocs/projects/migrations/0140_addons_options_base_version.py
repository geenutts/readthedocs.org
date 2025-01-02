# Generated by Django 4.2.16 on 2024-11-25 12:15

from django.db import migrations, models
import django.db.models.deletion
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.before_deploy

    dependencies = [
        ('builds', '0059_add_version_date_index'),
        ('projects', '0139_addons_filetreediff_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='addonsconfig',
            name='options_base_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='builds.version', verbose_name='Base version to compare against (eg. DocDiff, File Tree Diff)'),
        ),
        migrations.AddField(
            model_name='historicaladdonsconfig',
            name='options_base_version',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='builds.version', verbose_name='Base version to compare against (eg. DocDiff, File Tree Diff)'),
        ),
    ]