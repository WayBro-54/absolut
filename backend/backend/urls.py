from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # дублирование не хорошо...
    # нужно было сделать отдельную директорию под урлы...
    path("api/v1/", include("delivery.urls")),
    path("api/v1/", include("dictionaries.urls")),
    path("auth/", include("users.urls")),
]
