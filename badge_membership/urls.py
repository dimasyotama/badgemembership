from django.urls import path
from badge_membership.views import ProdukViewSet,ProfileViewSet,GetBadgeViewSet
from django.conf.urls import url

urlpatterns = [
    #url untuk list produk di toko serta detail produk
    url(r'^list_produk/$', ProdukViewSet.as_view({'get':'list'})),
    url(r'^list_produk/detail/(?P<pk>[0-9]+)/$', ProdukViewSet.as_view({'get':'details'})),

    #url untuk halaman profile
    url(r'^profile/$', ProfileViewSet.as_view({'get':'list'})),

    url(r'^get_badge/(?P<pk>[0-9]+)/$', GetBadgeViewSet.as_view({'get':'get_badge'}))


]
