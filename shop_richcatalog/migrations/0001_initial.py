# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to=b'rich_catalog', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='shop_richcatalog.Catalog', null=True)),
                ('products', models.ManyToManyField(related_name='catalogs', null=True, to='shop.Product', blank=True)),
            ],
            options={
                'verbose_name': 'Catalog',
                'verbose_name_plural': 'Catalogs',
            },
            bases=(models.Model,),
        ),
    ]
