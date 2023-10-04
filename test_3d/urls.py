
from django.contrib import admin
from django.urls import path, include

from test_3d import settings
from django.urls import path
from badges.views import UserBadgeAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('rest_authtoken.urls')),
    path('api/user_badges/<int:user_id>/', UserBadgeAPIView.as_view(), name='user_badges_api'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
