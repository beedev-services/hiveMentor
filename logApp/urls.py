from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.logDash),
    path('newWeek/', views.newWeek),
    path('createWeek/', views.createWeek),
    path('week/<int:week_id>/', views.viewWeek)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)