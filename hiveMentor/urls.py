from django.contrib import admin
from django.urls import path, include
from userApp import views as app_views
from chatApp import views as app_views
from logApp import views as app_views
from api import views as app_views
from recipesApp import views as app_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('coreApp.urls')),
    path('user/', include('userApp.urls')),
    path('logs/', include('logApp.urls')),
    path('chat/', include('chatApp.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('recipes/', include('recipesApp.urls')),
]