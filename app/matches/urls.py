from django.urls import path
from matches import views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('api/matches/', views.matches_list)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)