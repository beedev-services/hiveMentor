from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    # path('logReg/', views.logReg),
    # path('login/', views.login),
    # path('reg/', views.reg),
    # path('logout/', views.logout),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)