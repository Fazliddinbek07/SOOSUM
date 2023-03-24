from django.urls import path
from .views import *

urlpatterns = [
    path("get-info/", get_info),
    path("get-social-media/", get_social_media),
    path("create-order/", create_order),
    path("get-discount/", get_discount),
    path("get-product/", get_product),
    path("get-about-product/", get_about_product),
    path("get-about/", get_about),
    path("get-who-use/", get_who_use),
    path("get-how-to-use/", get_how_to_use),
    path("get-fact/", get_fact)
]