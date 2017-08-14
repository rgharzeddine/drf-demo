from django.conf.urls import url

from drf import views

from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    url(r'^api/products/$', views.ProductList.as_view()),
    url(r'^api/products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),

    url(r'^api/invoices/$', views.InvoiceList.as_view()),
    url(r'^api/invoices/(?P<pk>[0-9]+)/$', views.InvoiceDetail.as_view()),
]

urlpatterns += [
    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
