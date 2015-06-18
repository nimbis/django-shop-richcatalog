from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from shop_richcatalog.models import CatalogPlugin
from shop_richcatalog.models import Catalog


class CMSCatalogPlugin(CMSPluginBase):
    model = CatalogPlugin
    name = _("Catalog")
    render_template = "catalog/catalog_grid_plugin.html"

    def render(self, context, instance, placeholder):
        context['catalog_list'] = Catalog.objects.all()
        return context

plugin_pool.register_plugin(CMSCatalogPlugin)
