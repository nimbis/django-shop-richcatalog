from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from shop_richcatalog.models import CatalogPlugin


class CMSCatalogPlugin(CMSPluginBase):
    model = CatalogPlugin
    name = _("Catalog")
    render_template = "catalog/catalog_detail.html"

    def render(self, context, instance, placeholder):
        context['catalog'] = instance.catalog
        context['product_list'] = instance.catalog.products.filter(active=True).order_by('name')
        return context

plugin_pool.register_plugin(CMSCatalogPlugin)
