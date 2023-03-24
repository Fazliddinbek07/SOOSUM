from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("info-get/", info_get, name="info_get"),
    path("info-add/", info_add, name="info_add"),
    path("info-edit/", info_edit, name="info_edit"),
    path("info-delete/", info_delete, name="info_delete"),
    path("social-media-get/", social_media_get, name="social_media_get"),
    path("social-media-add/", social_media_add, name="social_media_add"),
    path("social-media-edit/<int:pk>/", social_media_edit, name="social_media_edit"),
    path("social-media-delete/<int:pk>/", social_media_delete, name="social_media_delete"),
    path("order-get/", order_get, name="order_get"),
    path("order-delete/<int:pk>/", order_delete, name="order_delete"),
]