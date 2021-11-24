from django.urls import path

from .views import preview, home, cartlist, lib, home, login_user, logout_user, register_user, cartupdate
urlpatterns = [
    path('preview/<int:idbook>', preview),
    path('library/<int:iduser>', lib, name='lib'),
    path('cart_update/<int:user>/<int:idbook>', cartupdate, name='cartupdate'),
    path('cart/<int:iduser>', cartlist, name='cartlist'),
    path('home/', home, name="home"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
]
