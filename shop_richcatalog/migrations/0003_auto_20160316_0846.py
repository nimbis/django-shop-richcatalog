# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('shop_richcatalog', '0002_catalogplugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='above_catalog_placeholder',
            field=cms.models.fields.PlaceholderField(related_name='above_catalog_placeholder', slotname=b'above_catalog_placeholder', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='catalog',
            name='below_catalog_placeholder',
            field=cms.models.fields.PlaceholderField(related_name='below_catalog_placeholder', slotname=b'below_catalog_placeholder', editable=False, to='cms.Placeholder', null=True),
        ),
    ]
