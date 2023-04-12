from django.urls import re_path
from matches import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^(?i)$', views.index.as_view(), name='matches'),
    re_path(r'^(?i)(?P<id>\d+)/?$', views.individual_match.as_view(), name='individual_match'),
    re_path(r'^(?i)api/all/?$', views.matches_list),
    re_path(r'^(?i)api/(?P<id>\d+)/?$', views.individual_match_api),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)