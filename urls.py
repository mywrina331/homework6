from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shrak_app.urls')),
    path('', include('app_lesson_4.urls')),
]

