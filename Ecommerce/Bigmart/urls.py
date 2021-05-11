from django.urls import path
from .views import *
urlpatterns=[
    path('register/',userregistration),
    path('login/',userlogin),
    path('logout/',userlogout),
    path('productspage/',productspage),
    path('productdetails/<int:id>/',productdetails),
    path('cart/<int:product_id>/',cartview),
    path('cartdetails/<int:id>/',cartdetails,name='cartdet'),
    path('delete/<int:product_id>/',deletecartdata),
    path('Home/',Home)
    ]