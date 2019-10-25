from django.urls import path

from . import views
# any that has listing/ should LOOK AT THIS file
urlpatterns = [
    path('', views.index, name='listings'), # третий параметр для удобного доступа к путю /listings
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),

]