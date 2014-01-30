from shop.views import ShopListView, ShopDetailView
from shop_richcatalog.models import Catalog
from shop.models import Product


class CatalogListView(ShopListView):
    '''
    Display all catalogs in a tree.
    '''

    model = Catalog
    template_name = 'catalog/catalog_list.html'
    context_object_name = 'catalog_list'


class CatalogDetailView(ShopDetailView):
    '''
    Display detailed catalog information.
    '''

    model = Catalog
    template_name = 'catalog/catalog_detail.html'
    context_object_name = 'catalog'

    def get_context_data(self, **kwargs):
        '''
        Get catalog context data.
        '''

        # get context data from superclass
        ctx = super(CatalogDetailView, self).get_context_data(**kwargs)

        # update the context with active products in this catalog
        product_list = self.object.products.filter(active=True)
        if product_list:
            ctx.update({"product_list": product_list})

        # return the context
        return ctx
