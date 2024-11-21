from django.contrib import admin
from django.urls import path, include

from homelog import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path( '',views.index,name="home"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),

]
