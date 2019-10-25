from django.contrib import admin
from django.urls import path, include

from django.conf import settings # для импорта фото из static/media folder
from django.conf.urls.static import static # и это тоже для избежания ошибок

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')), #any that has listings/ going to go to listings
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to show up photos
