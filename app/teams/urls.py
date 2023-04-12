from django.urls import re_path
from teams import views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^(?i)$', views.index.as_view(), name='teams'),
    re_path(r'^(?i)api/all/?$', views.teams_list, name='teams_list'),
    re_path(r'^(?i)api/(?P<abbreviation>[^/]+)/?$', views.individual_team, name='individual_team'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)