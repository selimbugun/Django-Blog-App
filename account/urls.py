from django.urls import path

from account import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('change-password/', views.change_password, name='change_password'),
    path('account/', views.account, name='account'),
    path('update-info/', views.update_info, name='update_info')
   
    
]
