# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_richcatalog', '0004_catalogplugin_root_catalog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='shop_richcatalog_catalogplugin', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
