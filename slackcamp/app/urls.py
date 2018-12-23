from django.urls import path,include
from app import views

app_name = 'app'
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('base/',views.base,name='base'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('materials/',views.materials,name='materials'),
    ]
