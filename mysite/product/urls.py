from django.urls import path
from product import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('',views.index1,name='index1'),
    path('addcomment/<int:id>',views.addcomment,name='addcomment'),
    path('AddToCart/<int:id>',views.AddToCart,name='AddToCart')
]
