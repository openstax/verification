from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
import profiles.urls
import oxauth.urls
from . import views

# Personalized admin site settings like title and header
admin.site.site_title = "Verification Site Admin"
admin.site.site_header = "Verification Administration"

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("users/", include(profiles.urls)),
    path("admin/", admin.site.urls),
    path(r'api/verify/', include(('verify.urls','verify'), namespace='verify')),
    path(r'oxauth/', include(('oxauth.urls', 'oxauth'), namespace='oxauth')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
