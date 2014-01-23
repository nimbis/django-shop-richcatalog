import os
from django.test import TestCase


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

        # TODO create sample products

    def tearDown(self):
        '''
        Tear down the test environment.
        '''

        # TODO delete sample products
        pass

    def test_crud(self):
        '''
        Create, store, update, and delete a category.
        '''

        # TODO
        pass
