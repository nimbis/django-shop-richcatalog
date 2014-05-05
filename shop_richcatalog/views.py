from shop.views import ShopListView, ShopDetailView
from shop_richcatalog.models import Catalog
from shop.models import Product
from django.conf import settings


class CatalogListView(ShopListView):
    '''
    Display all catalogs in a tree.
    '''

    model = Catalog
    template_name = 'catalog/catalog_list.html'
    context_object_name = 'catalog_list'

    def get_context_data(self, **kwargs):
        '''
        Conditionally add all products to top catalog.
        '''

        # get context data from superclass
        ctx = super(CatalogListView, self).get_context_data(**kwargs)

        # optionally update the context with all products
        if getattr(settings, 'RICHCATALOG_SHOW_ALL_PRODUCTS', True):
            products = Product.objects.filter(active=True).order_by('name')
            ctx.update({'product_list': products})

        # return the context
        return ctx


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
        products = self.object.products.filter(active=True).order_by('name')
        ctx.update({'product_list': products})

        # return the context
        return ctx
