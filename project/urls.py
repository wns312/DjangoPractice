from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("members/", include("members.urls")),
    path("orders/", include("orders.urls")),
    path("admin/", admin.site.urls),
]
