from django.db import models
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from shop_richcatalog.models import Catalog

from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _


class CatalogAdmin(MPTTModelAdmin):
    '''
    Admin model for catalogs.
    '''

    prepopulated_fields = {"slug": ("name",)}
    formfield_overrides = {
        models.ManyToManyField: {"widget": FilteredSelectMultiple(
            verbose_name=_("products"),
            is_stacked=False)}
    }

admin.site.register(Catalog, CatalogAdmin)
