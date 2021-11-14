from django.urls import path

from .views import preview, home, cartlist, lib
urlpatterns = [
    path('preview/<int:idbook>', preview),
    path('home', home),
    path('cartlist', cartlist),
    path('library', lib)

]
