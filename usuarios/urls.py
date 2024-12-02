from django.urls import path
from . import  views

urlpatterns = [

    path('registro/', views.registro_view, name="registro"),
    path('login/', views.login_view, name ='login'),
    path('logout/', views.UserLogoutView.as_view(), name ='logout'),
]
 
