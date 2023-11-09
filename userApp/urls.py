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
    path('profile/updateWeight/', views.updateWeight),
    path('profile/addZip/', views.addZip),
    path('profile/upgradeAccount/', views.upgradeAccount),
    path('forgotpassword/', views.forgotPassword),
    path('requestpasscode/', views.requestPassCode),
    path('password-reset/', views.passwordReset),
    path('reset-pass/', views.resetPass),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)