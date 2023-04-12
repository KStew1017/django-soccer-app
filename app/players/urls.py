from django.urls import re_path
from players import views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^(?i)$', views.index.as_view(), name='players'),
    re_path(r'^(?i)(?P<team>[^/]+)/?$', views.roster.as_view(), name='roster'),
    re_path(r'^(?i)api/all/?$', views.players_list),
    re_path(r'^(?i)api/(?P<id>\d+)/?$', views.individual_player),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
