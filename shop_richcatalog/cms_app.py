from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class RichCatalogApphook(CMSApp):
    name = _("Rich Catalog")
    urls = ["shop_richcatalog.urls"]


apphook_pool.register(RichCatalogApphook)
