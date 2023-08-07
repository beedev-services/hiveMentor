from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# All urls are at base /

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('dev-notes/', views.devNotes),
    path('logReg/', views.logReg),
    path('logout/', views.logout),
    path('choseRole/', views.choseRole),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)