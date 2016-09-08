django-shop-richcatalog
=======================

A rich catalog plugin for django shop.

[![Build Status](https://travis-ci.org/nimbis/django-shop-richcatalog.svg?branch=master)](https://travis-ci.org/nimbis/django-shop-richcatalog)

[![Coverage](https://coveralls.io/repos/nimbis/django-shop-richcatalog/badge.png?branch=master)](https://coveralls.io/r/nimbis/django-shop-richcatalog?branch=master)


Requirements
------------

* django-cms >= 3.3.1
* django-shop
* django-shop-richproduct


Installation
------------

* Run `pip install django-shop-richcatalog` or download this package and run `python setup.py install`

* Ensure that `django_shop_richcatalog` is in your INSTALLED APPS

* Run `syncdb` or `migrate django_shop_richcatalog` if you have South installed.

Contributing
------------

See the [Contributing Guidelines](CONTRIBUTING.md).

History
-------

v3.0.0:

    * Adding "root_catalog" field to the Catalog model. This allows a catalog
      plugin to display the contents of a catalog rather than displaying all
      catalogs.

v2.0.1:

    * Adding placeholder fields to the Catalog model. This allows the
      adding of CMS content below and above each catalog.

v2.0.0:

    * Now supports (requires) Django 1.8

    * Adds catalog name as "page_sub_title" for use in templates

v1.1.0:

    * Added missing migration.  New plugin for shop-richcatalog.

v1.0.0:

    * Django 1.7 is now supported.

v0.4.3:

    * Removing pip requirement from setup.py.

v0.1.0:

    * Initial version.
