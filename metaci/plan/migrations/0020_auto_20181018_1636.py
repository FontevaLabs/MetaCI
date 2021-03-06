# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-18 16:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("plan", "0019_merge_20180917_1855")]

    operations = [
        migrations.AlterModelOptions(
            name="planrepository",
            options={
                "base_manager_name": "objects",
                "ordering": ["repo", "plan"],
                "permissions": (
                    ("run_plan", "Run Plan"),
                    ("view_builds", "View Builds"),
                    ("rebuild_builds", "Rebuild Builds"),
                    ("qa_builds", "QA Builds"),
                ),
                "verbose_name_plural": "Plan Repositories",
            },
        )
    ]
