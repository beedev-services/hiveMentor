from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# All urls start with /user/
urlpatterns = [
    path('login/', views.login),
    path('reg/', views.reg),
    path('profile/', views.profile),
    path('profile/updateDiabetic/', views.updateDiabetic),
    path('profile/updateSleep/', views.updateSleep),
    path('profile/updateFood/', views.updateFood),
    path('profile/updateMood/', views.updateMood),
    path('profile/updateMeds/', views.updateMeds),
    path('profile/updateJournal/', views.updateJournal),
    path('profile/updateWeather/', views.updateWeather),
    path('profile/updateFitness/', views.updateFitness),
    path('profile/updateWork/', views.updateWork),
    path('profile/addZip/', views.addZip),
    path('profile/upgradeAccount/', views.upgradeAccount),
    path('theAdmin/', views.theAdmin),
    path('theAdmin/sendUsers/', views.sendUsers),
    path('theAdmin/getUsers/', views.getUsersChat),
    path('theAdmin/checkUser/', views.checkUser),
    path('theAdmin/theCodes/', views.theCodes),
    path('theAdmin/createCode/', views.createCode),
    # path('theAdmin/auth/', views.auth),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)