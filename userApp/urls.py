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
    path('profile/', views.profile),
    path('profile/updateDiabetic/', views.updateDiabetic),
    path('profile/updateSleep/', views.updateSleep),
    path('profile/updateFood/', views.updateFood),
    path('profile/updateMood/', views.updateMood),
    path('profile/updateMeds/', views.updateMeds),
    path('profile/updateJournal/', views.updateJournal),
    path('profile/upgradeAccount/', views.upgradeAccount),
    path('theAdmin/', views.theAdmin),
    path('theAdmin/sendUsers/', views.sendUsers),
    path('theAdmin/theCodes/', views.theCodes),
    path('theAdmin/createCode/', views.createCode),
    # path('theAdmin/auth/', views.auth),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)