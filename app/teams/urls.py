from django.urls import path
from teams import views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('api/teams/', views.teams_list, name='teams_list'),
    path('api/teams/<int:id>/', views.individual_team, name='individual_team')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)