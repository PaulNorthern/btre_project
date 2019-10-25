from django.urls import path

from . import views

# any that has listing/ should LOOK AT THIS file
urlpatterns = [
    path('login', views.login, name='login'), # третий параметр для удобного доступа к путю /listings
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),

]