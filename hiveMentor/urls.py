from django.contrib import admin
from django.urls import path, include
from userApp import views as app_views
from chatApp import views as app_views
from logApp import views as app_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('userApp.urls')),
    path('logs/', include('logApp.urls')),
    path('chat/', include('chatApp.urls')),
    path('admin/', admin.site.urls),
]
