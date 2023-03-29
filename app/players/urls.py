from django.urls import path
from players import views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('<str:team>/', views.roster.as_view(), name='roster'),
    path('api/players/', views.players_list),
    path('api/players/<int:id>/', views.individual_player)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
