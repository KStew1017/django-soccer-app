from django.urls import path
from matches import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('api/matches/', views.matches_list),
    path('api/matches/<int:id>/', views.individual_match)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)