from django.conf.urls import patterns, url
from shop_richcatalog.views import CatalogListView, CatalogDetailView

urlpatterns = patterns(
    "",
    url(r"^$",
        CatalogListView.as_view(),
        name="catalog_list"),
    url(r"^(?P<slug>[0-9A-Za-z-_.//]+)/$",
        CatalogDetailView.as_view(),
        name="catalog_detail")
)
