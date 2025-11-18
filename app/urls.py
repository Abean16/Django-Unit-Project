from django.urls import path
from .views import *
from app.views import login_view,storefront_page, register_view,logout_view


urlpatterns = [
    path('', login_view, name="login"),
    path('storefront/', storefront_page, name = "storefront"),
    path('register/', register_view, name = "register"),
    path('logout/', logout_view, name="logout")
]
