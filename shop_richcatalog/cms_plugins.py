from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from shop_richcatalog.models import CatalogPlugin
from shop_richcatalog.models import Catalog
from shop.models import Product


class CMSCatalogPlugin(CMSPluginBase):
    model = CatalogPlugin
    name = _("Catalog")
    render_template = "catalog/catalog_grid_plugin.html"

    def render(self, context, instance, placeholder):
        context = super(CMSCatalogPlugin, self).render(
            context, instance, placeholder)
        if instance.root_catalog:
            context['plugin_product_list'] = instance.root_catalog.products.\
                filter(active=True).order_by('name')
            context['plugin_catalog_list'] = \
                instance.root_catalog.children.all()
        else:
            context['plugin_product_list'] = Product.objects.none()
            context['plugin_catalog_list'] = Catalog.objects.all()
        return context

plugin_pool.register_plugin(CMSCatalogPlugin)
