from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    "",
    url('^shop/', include('shop.urls')),
    url('^catalog/', include('shop_richcatalog.urls'))
)
