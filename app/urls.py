from django.contrib import admin
from django.urls import path,include
from. import views

urlpatterns = [
    
    path("home/", views.home, name = "home"),
    path("register/", views.registerPage, name = "register"),
    path("", views.loginPage, name = "login"),
    path("logout/", views.logoutUser, name = "logout"),
]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


