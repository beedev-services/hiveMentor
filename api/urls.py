from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# All urls are at /api

urlpatterns = [
    path('', views.apiBase),
    path('allFoodData/', views.allFoodData),
    path('foodData/<str:cat>/', views.foodData),
    path('releaseDate/', views.releaseDates),
    path('userCount/', views.userCount),
    path('oneUser/<int:user_id>/', views.oneUser),
    path('trello/', views.board),
    path('testing/', views.testApi),
    path('loggedUser/<str:username>/', views.loggedUser),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)