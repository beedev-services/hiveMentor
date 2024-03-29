from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Main Landing for Logs
    path('', views.logDash),
    # create week
    path('createWeek/', views.createWeek),
    # Create List Bank Items
    path('createSymptom/', views.createSymptom),
    path('createMedication/', views.createNewMed),
    path('createWorkout/', views.createNewFitness),
    path('createNewFood/', views.createNewFood),
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
    # create water
    path('week/<int:week_id>/day/<int:day_id>/createWater/', views.createWater),
    # update water
    path('week/<int:week_id>/day/<int:day_id>/<int:water_id>/updateWater/', views.updateWater),
    # create Mood
    path('week/<int:week_id>/day/<int:day_id>/createMood/', views.createMood),
    # create Med
    path('week/<int:week_id>/day/<int:day_id>/createMed/', views.createMed),
    # create Weather
    path('week/<int:week_id>/day/<int:day_id>/createConditions/', views.createConditions),
    # create Food
    path('week/<int:week_id>/day/<int:day_id>/createFood/', views.createFood),
    # create Sugar
    path('week/<int:week_id>/day/<int:day_id>/createSugar/', views.createSugar),
    # create Weight
    path('week/<int:week_id>/day/<int:day_id>/createWeight/', views.createWeight),
    # create Sleep
    path('week/<int:week_id>/day/<int:day_id>/createSleep/', views.createSleep),
    # create Fitness
    path('week/<int:week_id>/day/<int:day_id>/createFitness/', views.createFitness),
    # create Work
    path('week/<int:week_id>/day/<int:day_id>/createWork/', views.createWork),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)