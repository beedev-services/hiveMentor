from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.chatDash),
    path('authenticate/<int:id>/', views.authenticate),
    path('multi-frame/<int:id>/', views.multiChatFrame),
    # Chat Admin
    path('theAdmin/', views.chatAdmin),
    path('theAdmin/sendUsers/', views.sendUsers),
    path('theAdmin/sendUsersGroups/', views.sendUsersGroup),
    path('theAdmin/getUsers/', views.getUsersChat),
    path('theAdmin/checkUser/', views.checkUser),
    path('theAdmin/getGroupMembers/', views.getGroupUsers),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)