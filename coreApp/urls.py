from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# All urls are at base /

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('dev-notes/', views.devNotes),
    path('logReg/', views.logReg),
    path('logout/', views.logout),
    path('choseRole/', views.choseRole),
    # Admin Routes
    path('theAdmin/', views.theAdmin),
    path('theAdmin/sendUsers/', views.sendUsers),
    path('theAdmin/getUsers/', views.getUsersChat),
    path('theAdmin/checkUser/', views.checkUser),
    path('theAdmin/theCodes/', views.theCodes),
    path('theAdmin/createCode/', views.createCode),
    # path('theAdmin/auth/', views.auth),
    # API Routes
    path('api/', views.apiBase),
    path('api/allFoodData/', views.allFoodData),
    path('api/foodData/<str:cat>/', views.foodData),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)