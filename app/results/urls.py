from django.urls import path
from results import views as views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index.as_view(), name='home'),
    path('api/results/', views.results_list),
    path('api/results/<int:id>/', views.individual_result)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)