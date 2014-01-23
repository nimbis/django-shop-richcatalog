from django.contrib import admin
from shop_richcatalog.models import Catalog
from django.utils.translation import ugettext_lazy as _


class CatalogAdmin(admin.ModelAdmin):
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
