from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('references',views.references,name='references'),
    path('contact',views.contact,name='contact'),
    path('category_detail/<int:id>/',views.category_detail,name='category_detail'),
    path('products/<int:id>/<slug:slug>/',views.products,name='products'),
    path('search/',views.search,name='search'),
    path('search_auto/',views.search_auto,name='search_auto'),
    path('logout/',views.logout,name='logout'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('edit',views.edit,name='edit'),
    
    







] 