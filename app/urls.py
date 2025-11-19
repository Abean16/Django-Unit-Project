from django.urls import path
from .views import *
from app.views import login_view,storefront_page, register_view,logout_view


urlpatterns = [
    path('', login_view, name="login"),
    path('storefront/', storefront_page, name = "storefront"),
    path('register/', register_view, name = "register"),
    path('logout/', logout_view, name="logout"),
    path('payment-success/<int:product_id>/', payment_succesful, name='payment-success'),
    path('payment-failed/<int:product_id>/', payment_failed, name='payment-failed'),
    path('checkout/<int:product_id>/', CreateCheckoutSessionView, name='checkout'),
    path('pricing/<int:product_id>/', pricing_view, name='pricing'),
]
