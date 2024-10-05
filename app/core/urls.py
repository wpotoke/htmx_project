from django.contrib import admin
from django.urls import re_path, path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("books.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
)

if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r"^rosetta/", include("rosetta.urls")),
    ]
