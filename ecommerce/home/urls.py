from django.urls import path
from .views import about, cart, login, signup, home

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'), 
    # path('logout/', logout, name='logout'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('', home, name='home'),
]
