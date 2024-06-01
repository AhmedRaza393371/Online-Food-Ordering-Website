from django.urls import path
from home.views import register, user_login, homepage, logout_view, landing, add_to_cart, view_cart, confirm_order,about_view,contact_view
from .views import clear_cart,review_view


urlpatterns = [
    path('landing/', landing, name='landing'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('homepage/', homepage, name='homepage'),
    path('logout/', logout_view, name='logout'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('confirm_order/', confirm_order, name='confirm_order'),
    path('clear_cart/', clear_cart, name='clear_cart'),  
    path('about/',about_view,name='about'),
    path('contact/',contact_view,name='contact'),
    path('review/',review_view,name='review'),
    
    
]
