from shop.views import ShopListView, ShopDetailView
from shop_richcatalog.models import Catalog
from shop.models import Product


class CatalogListView(ShopListView):
    '''
    TODO.
    '''

    model = Catalog
    #generic_template = "shop_richcatalog/catalog_list.html"

class CatalogDetailView(ShopDetailView):
    '''
    TODO.
    '''

    model = Catalog
    #generic_template = "shop_richcatalog/catalog_detail.html"

    def get_context_data(self, **kwargs):
        '''
        TODO.
        '''

        # get context data from superclass
        ctx = super(CatalogDetailView, self).get_context_data(**kwargs)

        # update the context with active products in this catalog
        product_list = self.object.products.filter(active=True)
        if product_list:
            ctx.update({"product_list": product_list})

        # return the context
        return ctx
