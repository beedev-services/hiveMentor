from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Main Landing for Logs
    path('', views.logDash),
    # create week
    path('createWeek/', views.createWeek),
    # view week
    path('week/<int:week_id>/', views.viewWeek),
    # edit week form
    path('week/<int:week_id>/edit/', views.editWeek),
    # edit week
    path('week/<int:week_id>/update/', views.updateWeek),
    # delete week function
    path('week/<int:week_id>/delete/', views.deleteWeek),
    # create day
    path('week/<int:week_id>/createDay/', views.createDay),
    # view day
    path('week/<int:week_id>/day/<int:day_id>/', views.viewDay),
    # create journal
    path('week/<int:week_id>/day/<int:day_id>/createJournal/', views.createJournal),
    path('week/<int:week_id>/day/<int:day_id>/createWater/', views.createWater),
    path('week/<int:week_id>/day/<int:day_id>/<int:water_id>/updateWater/', views.updateWater),
    path('week/<int:week_id>/day/<int:day_id>/createMood/', views.createMood),
    path('createSymptom/', views.createSymptom),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)