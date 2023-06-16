from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('logReg/', views.logReg),
    path('login/', views.login),
    path('reg/', views.reg),
    path('logout/', views.logout),
    path('choseRole/', views.choseRole),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)