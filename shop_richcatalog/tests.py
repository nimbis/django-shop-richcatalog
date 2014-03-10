import os
from django.test import TestCase
from django.test import Client
from shop_richcatalog.models import Catalog
from shop_richproduct.models import RichProduct


class SimpleTestCase(TestCase):
    '''
    Simple test cases that verifies basic model functionality.
    '''

    def setUp(self):
        '''
        Set up the test environment.
        '''

        # enable debug mode
        os.environ["DEBUG"] = "True"

        # create sample products
        product = RichProduct()
        product.name = "Apollo"
        product.slug = "apollo"
        product.active = True
        product.target = "http://www.google.com"
        product.save()

        product = RichProduct()
        product.name = "Aurora"
        product.slug = "aurora"
        product.active = True
        product.target = "http://www.google.com"
        product.save()

    def tearDown(self):
        '''
        Tear down the test environment.
        '''

        # delete sample products
        product = RichProduct.objects.get(slug="apollo")
        product.delete()

        product = RichProduct.objects.get(slug="aurora")
        product.delete()

    def test_crud(self):
        '''
        Create, store, update, and delete a catalog.
        '''

        # create a catalog
        catalog = Catalog()
        catalog.name = "Test Catalog"
        catalog.slug = "test-catalog"
        catalog.save()

        catalog.products.add(RichProduct.objects.get(slug="apollo"))
        catalog.products.add(RichProduct.objects.get(slug="aurora"))
        catalog.save()

        # retrieve the catalog
        catalog = None
        catalog = Catalog.objects.get(slug="test-catalog")

        # verify catalog fields
        self.assertEquals(catalog.name, "Test Catalog")
        self.assertEquals(catalog.slug, "test-catalog")
        self.assertEquals(len(catalog.products.all()), 2)

        # verify utility methods
        self.assertEquals(unicode(catalog), catalog.name)

        # get url
        self.assertEquals(catalog.get_absolute_url(), '/catalog/test-catalog/')

        # delete the catalog
        catalog.delete()
        catalog = None

    def test_catalog_views(self):
        '''
        Test the catalog list and detail views.
        '''
        # create a catalog
        catalog = Catalog()
        catalog.name = "Test Catalog"
        catalog.slug = "test-catalog"
        catalog.save()

        catalog.products.add(RichProduct.objects.get(slug="apollo"))
        catalog.products.add(RichProduct.objects.get(slug="aurora"))
        catalog.save()

        client = Client(enforce_csrf_checks=True)
        response = client.get(catalog.get_absolute_url())
        self.assertEquals(response.context['catalog'].name, "Test Catalog")
        self.assertEquals(len(response.context['product_list']), 2)
