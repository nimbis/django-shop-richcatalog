from django.db import models
from shop.models import Product
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Catalog(models.Model):
    '''
    A catalog of products with a description and thumbnail image.
    '''

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    products = models.ManyToManyField(Product, related_name="catalogs")
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="rich_catalog")

    class Meta(object):
        verbose_name = _("catalog")
        verbose_name_plural = _("catalogs")

    def get_absolute_url(self):
        return reverse("catalog_detail", args=[self.slug])

    def __unicode__(self):
        return self.name
