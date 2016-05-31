# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_richcatalog', '0003_auto_20160316_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogplugin',
            name='root_catalog',
            field=models.ForeignKey(blank=True, to='shop_richcatalog.Catalog', null=True),
        ),
    ]
