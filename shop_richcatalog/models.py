from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from shop.models import Product
from cms.models import CMSPlugin

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Catalog(MPTTModel):
    '''
    A catalog of products with a description and thumbnail image.
    '''

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    parent = TreeForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children")

    products = models.ManyToManyField(
        Product,
        null=True,
        blank=True,
        related_name="catalogs")

    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="rich_catalog", null=True, blank=True)

    class Meta(object):
        verbose_name = _("Catalog")
        verbose_name_plural = _("Catalogs")

    class MPTTMeta(object):
        order_insertion_by = ["slug"]

    def get_absolute_url(self):
        return reverse("catalog_detail", args=[self.slug])

    def __unicode__(self):
        return self.name


class CatalogPlugin(CMSPlugin):
    title = models.CharField(max_length=50)
