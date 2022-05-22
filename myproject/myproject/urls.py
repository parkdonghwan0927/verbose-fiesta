from django.contrib import admin
from django.urls import path, include
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('calendar/', views.calendar),
    path('profile/', include('users.urls')),
]
