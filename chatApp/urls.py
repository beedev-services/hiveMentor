from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.chatDash),
    path('authenticate/<int:id>/', views.authenticate),
    path('frame/<int:id>/', views.chatFrame),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)