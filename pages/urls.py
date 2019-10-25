from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # третий параметр для удобного доступа к путю
    path('about', views.about, name='about'),


]